from flask import Flask, render_template
from mongoengine import StringField, IntField, BooleanField, Document
import mlab
from models.service import Service
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/age')
def age():
    all_service = Service.objects(yob__gte=1990,address="Hà Nội")
    return render_template('age.html',all_service=all_service)

@app.route("/search/<g>")
def search(g):
    all_service = Service.objects(gender=g)
    return render_template('search.html',all_service=all_service)

@app.route("/delete/<id>")
def delete(id):
    Service.objects.get(id=id).delete()
    all_service = Service.objects()
    return render_template('search.html',all_service=all_service)

@app.route("/get/<id>")
def get(id):
    all_service = Service.objects(id=id)
    return render_template('search.html',all_service=all_service)

if __name__ == '__main__':
  app.run( debug=True)
