from flask import Flask, render_template, redirect, request
from wtforms import StringField
from flask_wtf import FlaskForm


class BaseLogin(FlaskForm):
    username = StringField('UserName: ')
    password = StringField('Password: ')


app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET'])
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def baselogin():
    username = request.form['username'] if request.method == 'POST' else None
    password = request.form['password'] if request.method == 'POST' else None
    form = BaseLogin({})
    print(request.method, username, password)
    # return redirect('login', form=form)   # error
    if request.method == 'POST':
        return redirect('login')
    return render_template('login.html', form=form)


app.run(port=2000)