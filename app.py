from flask import Flask
from flask import request,render_template



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template("form_signin.html")

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'dhduan' and password == '111':
        return render_template("signin-ok.html",username=username)
    return render_template("form_signin.html",message="Bad username or password",username=username)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
