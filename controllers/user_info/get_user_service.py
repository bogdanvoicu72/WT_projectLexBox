import os

from bson import ObjectId
from flask import render_template, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_mail import Message

from common.response_builder import ResponseBuilder
from common.key_builder import KeyBuilder


def get_user_service(request, users):
    try:
        user = users.find_one({"_id": ObjectId(request['uid'])})

        user_info = {
            "firstName": user['firstName'],
            "lastName": user['lastName'],
            "email": user['email'],
            "ci": user['ci'],
            "address": user['address']
        }

        return ResponseBuilder.success({"user": user_info})
    except Exception as e:
        return ResponseBuilder.failure(str(e))
