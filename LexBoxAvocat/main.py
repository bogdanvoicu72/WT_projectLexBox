from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cereri=[{
    "nume":"dl",
    "inspectorat":"u",
    "data":"8765",
    "status":"noua",
    "id":1
},
    {
        "nume": "dl",
        "inspectorat": "u",
        "data": "8765",
        "status": "noua",
        "id": 2
    },
{
        "nume": "dl",
        "inspectorat": "u",
        "data": "8765",
        "status": "progres",
        "id": 3
    },
{
        "nume": "dl",
        "inspectorat": "u",
        "data": "8765",
        "status": "terminata",
        "id": 4
    }
]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return redirect('/')

@app.route('/')
def home():
    return render_template('home.html', cereri=cereri)


if __name__ == '__main__':
    app.run(port=5002)

