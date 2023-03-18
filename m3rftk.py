from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
app = Flask(__name__)
path = os.path.abspath(os.getcwd())+r"\blog.db"


import requests
import json

headers = {
  'Content-Type': 'application/json',
  'customer-id': '1912912178',
  'x-api-key': 'z*****************************************'
}
def send_message(Text: str):
    payload = json.dumps({
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": Text
        }
      ]
    })
    response = requests.post("https://experimental.willow.vectara.io/v1/chat/completions", headers=headers, data=payload)
    Result = response.json()['choices'][0]['message']['content']
    return Result



@app.route('/')
def index():
        return render_template('index.html')
@app.route('/<name>')
def name(name):
        return render_template(name)
@app.route('/first')
def standerd():
        return render_template('firstart.html')

@app.route('/send')
def send():
    return render_template('contact.html')
@app.route('/send-m',methods = ['POST'])
def msg():
    message= request.form['cMessage']
    message= send_message(f'translate this to arabic {message}')
    return render_template('temp.html',message=message)
if __name__ == '__main__':
    app.run(debug=True)