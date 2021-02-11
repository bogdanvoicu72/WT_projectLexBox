import os
import uuid

from bson import ObjectId
from docxtpl import DocxTemplate
from flask import render_template
from flask_jwt_extended import get_jwt_identity
from flask_mail import Message

from common.response_builder import ResponseBuilder


def upload_files(files, minio_client, user):
    filenames = []
    file_name = ''
    for file in files:
        extension = str(files[file].filename).split(".")[-1]
        if str(file).__contains__("imagine_chitanta_plata"):
            file_name = f'Cerere-{user["firstName"]}-{user["lastName"]}-CHITANTA-PLATA-{str(uuid.uuid1())}.{extension}'
            minio_client.upload_fileobj(files["imagine_chitanta_plata"], 'lexbox', file_name)
        if str(file).__contains__("carte_de_identitate"):
            file_name = f'Cerere-{user["firstName"]}-{user["lastName"]}-CARTE_IDENTITATE-{str(uuid.uuid1())}.{extension}'
            minio_client.upload_fileobj(files["carte_de_identitate"], 'lexbox', file_name)
        if str(file).__contains__("imagine_proces_verbal"):
            file_name = f'Cerere-{user["firstName"]}-{user["lastName"]}-PROCES_VERBAL-{str(uuid.uuid1())}.{extension}'
            minio_client.upload_fileobj(files["imagine_proces_verbal"], 'lexbox', file_name)
        if str(file).__contains__("imagine_orice_alta_imagine"):
            for other_file in files.getlist("imagine_orice_alta_imagine"):
                file_name = f'Cerere-{user["firstName"]}-{user["lastName"]}-ALTE-IMAGINI-{str(uuid.uuid1())}.{extension}'
                minio_client.upload_fileobj(other_file, 'lexbox', file_name)
        filenames.append(file_name)

    return filenames


def build_record_output(request_json, filenames, user):
    result = dict(request_json)
    result['docx'] = request_json['docx']
    result['filenames'] = filenames
    result['status_dosar'] = 'new'

    return result


def insert_service(request_json, files, users, records, minio_client):
    try:
        user = users.find_one({"_id": ObjectId(request_json['uid'])})
        filenames = upload_files(files=files, user=user, minio_client=minio_client)
        result = build_record_output(request_json=request_json, filenames=filenames, user=user['_id'])

        records.insert_one(result)

        return ResponseBuilder.success({"msg": "Successfully uploaded"})
    except Exception as e:
        print(str(e))
        return ResponseBuilder.failure(str(e))
