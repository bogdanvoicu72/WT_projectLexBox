import os
import uuid

from bson import ObjectId
from docxtpl import DocxTemplate
from flask import render_template
from flask_jwt_extended import get_jwt_identity
from flask_mail import Message

from common.response_builder import ResponseBuilder


def build_document_input(user, request_json):
    return {
        "law": request_json.get('lege', None),
        "first_name": user['firstName'],
        "last_name": user['lastName'],
        "address": user['address'],
        "ci": user['ci'],
        "assisted": request_json.get('asistat_avocat', None),
        "accused": {
            'name': request_json.get('institutia_agent', None),
            'address': {
                'city': request_json.get('accused_city', None),
                'street': request_json.get('accused_street', None),
                'number': request_json.get('accused_number', None),
                'county': request_json.get('accused_county', None)
            },
            'code': '515607',
            'phone': request_json.get('accused_phone', None),
            'fax': request_json.get('accused_phone', None),
            'email': request_json.get('accused_email', None)
        },
        "record": {
            'series': request_json.get('record_series', None),
            'number': request_json.get('record_number', None),
            'date': request_json.get('record_date', None),
            'communication_date': request_json.get('record_communication', None)
        },
        "fine": request_json.get('valoarea_amenzii', None),
        "sanction": "Sanctiune",
        "agreed_to_sanction": 1,
        "witnesses": []
    }


def generate_service(request_json, users, mail, minio_client, owner_email):
    try:
        doc = DocxTemplate("templates/request.docx")
        user = users.find_one({"_id": ObjectId(request_json['uid'])})

        context = build_document_input(user, request_json)
        print(context)
        doc.render(context)
        doc.save("result.docx")
        file_name = f'Cerere-{user["firstName"]}-{user["lastName"]}-{str(uuid.uuid1())}.docx'
        with open("result.docx", "rb") as f:
            minio_client.upload_fileobj(f, 'lexbox', file_name)
        os.remove('result.docx')
        download_link = f'http://localhost:9000/lexbox/{file_name}'

        msg = Message('Notificare LexBox', sender=os.getenv('EMAIL'), recipients=[owner_email])
        msg.html = render_template("NotificationEmail.html",
                                   firstName=user['firstName'],
                                   lastName=user['lastName'],
                                   documentUrl=download_link)
        mail.send(msg)
        return ResponseBuilder.success({"download_link": download_link, 'filename': file_name})
    except Exception as e:
        print(str(e))
        return ResponseBuilder.failure(str(e))
