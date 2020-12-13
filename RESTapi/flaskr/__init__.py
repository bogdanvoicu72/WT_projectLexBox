import os

from flask import Flask
from flask import request

# At first running, run next two commands(for windows). For linux/mac check official Flask documentation
# set FLASK_APP=flaskr
# set FLASK_ENV=development

# To start flask rest api run command: flask run


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    import RESTapi.services.database_connection as dbs
    import RESTapi.services.validate as validate

    #app.register_blueprint(services)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello', methods=['POST'])
    def hello():
        req_data = request.get_json()

        database = dbs.connect("lexbox")

        if database is not None:
            collection = database["lexbox_data"]

            if validate.validate(req_data):
                collection.insert_one(req_data)
            else:
                print("ERROR: JSON data is not valid!")

            print(collection)
        else:
            print("Database is None")

        return ""

    @app.route('/')
    def index():
        return '<a href="/hello">Hello Page</a>'

    return app
