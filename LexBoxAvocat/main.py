import json
import os
import requests

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

cereri=[]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        response = requests.post("http://127.0.0.1:5000/login_avocat", request.form)

        if response.status_code == 200:
            session["logged_in"] = True
            return redirect("/")

        if response.status_code == 401:
            # incorrect password
            pass

    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if session.get("logged_in") is True:
        cereri = []
        response = requests.post("http://127.0.0.1:5000/get_records", request.form)
        result = response.json()["records"]

        result = result.replace("'", '"')
        result = json.loads(result)

        count = 1

        for res in result:
            cereri.append(
                {
                    "id": count,
                    "nume": res["user"],
                    "inspectorat": res["inspectorat"][0],
                    "data": res["data"][0],
                    "status": res["status"],
                    "docx": "http://localhost:9000/lexbox/" + res["docx"],
                    "files": []
                }
            )

            count_files = 1
            for file in res["files"]:
                cereri[count-1]["files"].append(
                    {
                        "filename": "Fisier " + str(count_files),
                        "link": "http://localhost:9000/lexbox/" + file
                    }
                )
                count_files += 1

            count += 1

        return render_template('home.html', cereri=cereri)
    else:
        return redirect("/login")


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(port=5002)

