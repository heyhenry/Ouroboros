from flask import Flask, render_template, redirect, url_for, request, session
import requests
import json
from datetime import datetime

app = Flask(__name__)
# app.secret_key = ''

@app.route('/', methods=['GET', 'POST'])
def login():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run()