import os
import uuid

from docxtpl import DocxTemplate
from flask import render_template
from flask_jwt_extended import get_jwt_identity
from flask_mail import Message

from common.response_builder import ResponseBuilder


def build_document_input(user, request_json):
    return {
        "law": str(request_json.get('articolul', None)) + "/" + str(request_json.get('alineatul', None)),
        "first_name": request_json.get('nume', None),
        "last_name": request_json.get('prenume', None),
        "address": request_json.get('adresa_procedurala', None),
        "assisted": request_json.get('asistat_avocat', None),
        "record": request_json.get('record', None),
        "fine": request_json.get('amenda_platita', None),
        "sanction": "",
        "agreed_to_sanction": request_json.get('dorinta_amenda', None),
    }


def generate_service(request_json, users, mail, minio_client, owner_email):
    try:
        doc = DocxTemplate("templates/request.docx")
        context = build_document_input(None, request_json)
        doc.render(context)
        doc.save("result.docx")
        file_name = 'asd.docx'
        with open("result.docx", "rb") as f:
            minio_client.upload_fileobj(f, 'lexbox', file_name)
        os.remove('result.docx')
        download_link = f'http://localhost:9000/lexbox/{file_name}'

        msg = Message('Notificare LexBox', sender=os.getenv('EMAIL'), recipients=[owner_email])
        msg.html = render_template("NotificationEmail.html",
                                   firstName="user['firstName']",
                                   lastName="user['lastName']",
                                   documentUrl=download_link)
        mail.send(msg)
        return ResponseBuilder.success({"download_link": download_link})
    except Exception as e:
        print(e)
        return ResponseBuilder.failure(str(e))
