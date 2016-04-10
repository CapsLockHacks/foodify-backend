from flask import Flask, redirect, url_for, session, request,send_file,render_template
from flask_oauthlib.client import OAuth, OAuthException
import sys
import logging
import os
import requests

from parse_rest.connection import register, SessionToken
from parse_rest.datatypes import Object
from parse_rest.user import User


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.debug = True
app.secret_key = 'development'

register('O6H2V7pJzoOWntRT9hFqpxxHHdJTCLtA7xmnhHZ5', 'olPs7M45S8mx7RpdSOSbAqfZbfBKjLzDzqISSivP', master_key='ZSpZtkfRzOziXOOJEy9kGjaTDVaju64YQcbLeBRH')


@app.route('/')
def index():
    if 'auth_token' in session:
        r = requests.get('http://hacknsit.herokuapp.com/user/calories/'+session["auth_token"]).json()

        return render_template('result.html',calories=r)

    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		user_name = request.form['user']
		password  = request.form['password']

	u = User.login(user_name, password)
	session["auth_token"] = u.sessionToken
	session["user_namFriende"] = u.username
    return render_template('result.html',calories=r)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
