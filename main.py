#create basic flask app / rest api

from flask import Flask, render_template, request, redirect, url_for, flash
import json


import os
template_dir = os.path.abspath('./pages')
app = Flask(__name__,template_folder='./pages')

@app.route('/')
def index():
    return render_template('index.html')

#/get
@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    if userText == '':
        return json.dumps({'status':'ERROR', 'answer':'Please enter a valid answer'})
    else:
        return json.dumps({'status':'OK', 'answer':'Hello, I am a chatbot. I am here to answer your questions'})

#run the app
if __name__ == '__main__':
    app.run(debug=True,port=5000)
