# LexBox API
The api of the LexBox app. It is written in Flask and implements JWT authentification.

## Routes
These are the routes the api currently supports:
* `/login` -> POST -> logins the user
* `/register` -> POST -> registers the user
* `/refresh` -> POST -> creates a new access token
* `/confirm_email` -> POST -> confirms a user's email
* `/generate` -> POST -> generates a document

## Environment variables
The LexBox project uses a couple of `environment variables` that have to be added to
a `.env` file in the project's root directory. These are:
* SECRET -> flask secret
* EMAIL -> gmail address used for the emailing service
* PASSWORD -> the password for the above email address
* URL -> url of where the application is running
* MONGO_USER -> the mongodb user 
* MONGO_PASSWORD -> the mongodb password
* OWNER_EMAIL -> the email of the application owner
* MINIO_ACCESS_KEY -> the access key for Minio 
* MINIO_SECRET_KEY -> the secret key for Minio

### Note
Default values for `Mongo` and `Minio` can be found in the `docker-compose.yml` file.
## Running the app
First make sure to have MongoDb and Minio instances running. They can both be 
bootstrapped by using [docker-compose](https://docs.docker.com/compose/), specifically
by running `docker-compose up` from the project's root directory.
Otherwise, both Minio and MongoDb have to be manually installed and configured to use
the same `environment variables` as present in the `docker-compose.yml` file.  

Also, bear in mind that the following commands apply to UNIX-like systems,
like Linux and MacOS. If using Windows, go ask Billie for help. 

* Open up a terminal
* Navigate to the project's root directory
* Run: `python3 -m venv venv`
* Run: `source venv/bin/activate`
* Run: `pip3 install -r requirements.txt`
* Run: `python3 main.py`
