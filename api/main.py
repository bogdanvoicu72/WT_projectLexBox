from flask import request
from flask_jwt_extended import (
    jwt_required, jwt_refresh_token_required
)

from config.setup import setup
from controllers.main import Controller

app, mail, jwt, users, records, minio_client, owner_email = setup()


@app.route('/login', methods=['POST'])
def login():
    return Controller.login(request_form=request.form, users=users)


@app.route('/register', methods=['POST'])
def register():
    return Controller.register(request_form=request.form, users=users, mail=mail)


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    return Controller.refresh()


@app.route('/confirm_email', methods=['GET'])
@jwt_required
def confirm():
    return Controller.confirm(request_form=request.form, users=users)


@app.route('/generate_document', methods=['POST'])
def generate():
    return Controller.generate(request_json=request.form, users=users, mail=mail, minio_client=minio_client,
                               owner_email=owner_email)


@app.route('/insert_record', methods=['POST'])
def insert():
    return Controller.insert(request_json=request.form, files=request.files, users=users, records=records, minio_client=minio_client)


if __name__ == '__main__':
    app.run()
