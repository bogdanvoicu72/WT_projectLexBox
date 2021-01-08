from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return redirect('/')

@app.route('/')
def home():
    return 'home'


if __name__ == '__main__':
    app.run(port=5002)

