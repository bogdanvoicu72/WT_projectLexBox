from controllers.confirmation.confirm_service import confirm_service
from controllers.generation.generate_service import generate_service
from controllers.insert.insert_service import insert_service
from controllers.login.login_service import login_service
from controllers.refresh.refresh_service import refresh_service
from controllers.register.register_service import register_service
from controllers.user_info.get_user_service import get_user_service


class Controller:
    @staticmethod
    def register(request_form, users, mail):
        return register_service(request_form, users, mail)

    @staticmethod
    def login(request_form, users):
        return login_service(request_form, users)

    @staticmethod
    def refresh():
        return refresh_service()

    @staticmethod
    def confirm(request_form, users):
        return confirm_service(request_form, users)

    @staticmethod
    def generate(request_json, users, mail, minio_client, owner_email):
        return generate_service(request_json, users, mail, minio_client, owner_email)

    @staticmethod
    def insert(request_json, users, files, records, minio_client):
        return insert_service(request_json, files, users, records, minio_client)\

    @staticmethod
    def user_info(request, users):
        return get_user_service(request, users)
