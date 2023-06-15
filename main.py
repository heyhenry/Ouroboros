from flask import Flask, render_template, redirect, url_for, request, session
import requests
import json
from datetime import datetime

app = Flask(__name__)
# app.secret_key = ''

# functions

# check user's entered login credentials
def check_login_credentials(username, password):

    # temporary roleplaying db stored credentials:
    db_username = 'yaka' 
    db_password = 'waka'

    if username == db_username and password == db_password:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def login():
    
    error = None

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if check_login_credentials(username, password):

            return redirect(url_for('forum'))

        else:
            error = 'Unsuccessful login. Please try again.'

    return render_template('login.html', error=error)
    
@app.route('/forum', methods=['GET', 'POST'])
def forum():

    return render_template('forum.html')

if __name__ == '__main__':
    app.run()