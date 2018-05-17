from flask import Flask, render_template, redirect, url_for, request
from mongoengine import StringField, IntField, BooleanField, Document
import mlab
from models.service import Service
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/delete_all")
def delete_all():
    all_service = Service.objects()
    for service in all_service:
        service.delete()
    return render_template('search.html')

if __name__ == '__main__':
  app.run( debug=True)
