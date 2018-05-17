from flask import Flask, render_template, redirect, url_for, request
from mongoengine import StringField, IntField, BooleanField, Document
import mlab
from models.service import Service
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service=all_service)

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

# @app.route("/delete1/<service_id>")
# def delete1(service_id):
#     Service.objects.get(id=service_id).delete()
#     all_service = Service.objects()
#     return render_template('admin.html',all_service=all_service)
@app.route("/delete1/<service_id>")
def delete1(service_id):
    id_del=Service.objects.with_id(service_id)
    if id_del is not None:
        id_del.delete()
    return redirect(url_for('admin'))

@app.route('/new-service',methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        new_service = Service(name=name, yob=yob)
        new_service.save()
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run( debug=True)
