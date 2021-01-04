import os

from flask import render_template
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_mail import Message

from common.response_builder import ResponseBuilder


def build_user_input(request_form):

    return {
        "firstName": request_form['firstName'],
        "lastName": request_form['lastName'],
        "email": request_form['email'],
        "barou": request_form['barou'],

    }


def register_service_avocat(request_form, users, mail):
    try:
        email = request_form['email']
        if users.find_one({"email": email}) is not None:
            return ResponseBuilder.failure("Email already exists", 401)
        msg = Message('Bun venit de la LexBox', sender=os.getenv('EMAIL'), recipients=[email])
        msg.html = render_template("ConfirmationEmail.html",
                                   firstName=request_form['firstName'],
                                   lastName=request_form['lastName'],
                                   confirmationUrl=f'{os.getenv("URL")}/confirm_email?email={email}')
        mail.send(msg)
        users.insert_one(build_user_input(request_form))
        access_token = create_access_token(identity=email),
        refresh_token = create_refresh_token(identity=email)
        return ResponseBuilder.success({"access_token": access_token, "refresh_token": refresh_token})
    except Exception as e:
        return ResponseBuilder.failure(str(e))
