from flask import Flask, redirect, url_for, session, request,send_file,render_template
from flask_oauthlib.client import OAuth, OAuthException
import sys
import logging
import os
import requests


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.debug = True
app.secret_key = 'development'

@app.route('/')
def index():
    if 'oauth_token' in session:
        r = requests.get('http://hacknsit.herokuapp.com/user/calories').json()

        return render_template('result.html',calories=r)

    else:
        return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
