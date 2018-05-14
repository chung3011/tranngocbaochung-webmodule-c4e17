from flask import Flask, render_template
from mongoengine import *
from models.customer import Customer
import mlab

app = Flask(__name__)

# Connect database
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def search():
    all_customer = Customer.objects()
    return render_template('search.html', all_customer=all_customer)

@app.route('/find/<g>')
def find(g):
    all_customer = Customer.objects[:10](contacted=False, gender =g)
    return render_template('search.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
