#!flask/bin/python
import sys
import datetime
import os
from flask import Flask, jsonify, make_response, request, render_template, url_for,redirect
from flask import send_from_directory

import db

app = Flask(__name__)
authorized_tokens = {}
app.config['UPLOAD_FOLDER'] = '/Users/Asim/Downloads'


@app.route('/')
def mainPage():
    return render_template('index.html')


@app.route('/handle_form', methods=['POST'])
def upload_file():
    file = request.files['file']

    if request.method == 'POST':
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('view_file',
                                filename=filename))


## merge with database
@app.route('/uploads/<filename>')
def view_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)




if __name__ == '__main__':

    # Run app
    app.run(debug=False, host='localhost', port=8080)
