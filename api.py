import os
import requests as re
from flask import Flask, jsonify, request, redirect, url_for
from flask.ext.cors import CORS

from werkzeug import secure_filename

import cloudsight

auth = cloudsight.SimpleAuth('qAd-COIpRxvKVaNUKrJMMQ')
api = cloudsight.API(auth)


UPLOAD_FOLDER = 'tmp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def helloWorld():
  return "Hello, world! <a href='https://github.com/CapsLockHacks/hackNSIT-backend'>Fork me on GitHub!</a>"

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            #with open(file, 'rb') as f:
            response = api.image_request(file, file.filename, {
                'image_request[locale]': 'en-US',
            })

            status = api.image_response(response['token'])
            if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
                # Done!
                pass
            status = api.wait(response['token'], timeout=30)

            print(status)

            return jsonify(result=status.name)


    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
