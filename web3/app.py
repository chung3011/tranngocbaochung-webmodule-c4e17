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
    return render_template('service.html')

@app.route("/delete/<service_id>")
def delete(service_id):
    id_del=Service.objects.with_id(service_id)
    if id_del is not None:
        id_del.delete()
    return redirect(url_for('admin'))

@app.route('/service')
def service_list():
    all_service = Service.objects()
    return render_template('service.html', all_service=all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service=service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service=all_service)

@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        service = Service(name=name, yob=yob, phone=phone, gender=gender)
        service.save()
        return redirect(url_for('admin'))

@app.route('/update/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    if request.method == 'GET':
        service = Service.objects.with_id(service_id)
        return render_template ('update.html', service=service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        status = form['status']
        description = form['description']
        measurements = form['measurements']
        image = form['image']
        service = Service.objects.with_id(service_id)
        service.update(set__name=name,
                                    set__yob=yob,
                                    set__gender=gender,
                                    set__height=height,
                                    set__phone=phone,
                                    set__address=address,
                                    set__status=status,
                                    set__description=description,
                                    set__measurements=measurements,
                                    set__image=image)
        service.reload()
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run( debug=True)
