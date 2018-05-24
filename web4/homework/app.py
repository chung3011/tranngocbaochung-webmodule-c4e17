from flask import *
from mongoengine import *
import mlab
import datetime
from gmail import GMail, Message
from models.service import Service
from models.user import User
from models.order import Order
app = Flask(__name__)
app.secret_key = "123456789"
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service')
def service_list():
    all_service = Service.objects()
    return render_template('service.html', all_service=all_service)

@app.route('/find/<g>')
def find(g):
    all_service = Service.objects(status=False, gender=g)
    return render_template('service.html', all_service=all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    if "loggedin-user" in session:
        service = Service.objects.with_id(service_id)
        return render_template('detail.html', service=service)
    else:
        return redirect(url_for("login"))

@app.route('/order/<service_id>')
def order(service_id):
    if "loggedin-user" in session:
        service = Service.objects.with_id(service_id)
        order = Order(service_name=service.name, service_user=session['account'], time=datetime.datetime.now(), is_accepted=False)
        order.save()
        return 'done'
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=["GET","POST"])
def login():
    if ("loggedin" in session) or ("loggedin-user" in session):
        return render_template('error.html')
    else:
        if request.method == "GET":
            return render_template('login.html')
        elif request.method == "POST":
            form = request.form
            username = form['username']
            password = form['password']
            if username=='' or password=='':
                return render_template('error.html')
            if username =='admin' and password == 'admin':
                session['loggedin'] = "admin"
                return redirect(url_for("admin"))
            else:
                user = User.objects(account = username, password = password)
                if user:
                    session['loggedin-user'] = "user"
                    session['account'] = username
                    session['password'] = password
                    return redirect(url_for("index"))
                else:
                    return render_template('error.html')

@app.route('/logout')
def logout():
    if 'loggedin' in session:
        del session['loggedin']
        return redirect(url_for("index"))
    elif 'loggedin-user' in session:
        del session['loggedin-user']
        del session['account']
        del session['password']
        return redirect(url_for("index"))
    else:
        return render_template('error.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        account = form['account']
        password = form['password']
        if name == '' or email=='' or account=='' or password=='':
            return render_template('error.html')
        if account =='admin' and password == 'admin':
            return render_template('error.html')
        else:
            user = User.objects(account = account)
            if user:
                return render_template('error.html')
            else:
                user = User(name=name, email=email, account=account, password=password)
                user.save()
                if user:
                    session['loggedin-user'] = "user"
                    session['account']=account
                    session['password']=password
                    return redirect(url_for('index'))
                else:
                    return render_template('error.html')

@app.route('/admin')
def admin():
    if "loggedin" in session:
        all_service = Service.objects()
        return render_template('admin.html', all_service=all_service)
    else:
        return redirect(url_for("login"))

@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if "loggedin" in session:
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
    else:
        return redirect(url_for("login"))

@app.route('/update/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    if "loggedin" in session:
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
                            set__status=bool(status),
                            set__description=description,
                            set__measurements=measurements,
                            set__image=image)
            service.reload()
            return redirect(url_for('admin'))
    else:
        return redirect(url_for("login"))

@app.route("/delete/<service_id>")
def delete(service_id):
    if "loggedin" in session:
        id_del=Service.objects.with_id(service_id)
        if id_del is not None:
            id_del.delete()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for("login"))

@app.route('/order_list')
def order_list():
    if "loggedin" in session:
        all_order = Order.objects()
        return render_template('order.html', all_order=all_order)
    else:
        return redirect(url_for("login"))

@app.route('/accept/<order_id>')
def accept(order_id):
    if "loggedin" in session:
        order = Order.objects.with_id(order_id)
        order.update(set__is_accepted=True)
        gmail = GMail('20150413@student.hust.edu.vn','chung20150413')
        msg = Message('Test Message',to='chung.hitc97@gmail.com',text='Hello')
        all_order = Order.objects()
        return render_template('order.html', all_order=all_order)
    else:
        return redirect(url_for("login"))

if __name__ == '__main__':
  app.run( debug=True)
