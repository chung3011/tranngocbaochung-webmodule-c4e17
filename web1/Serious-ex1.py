from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

@app.route('/bmi/<int:w>/<int:h>')

def index(w,h):
    h/=100
    bmi= round((w/(h*h)),2)
    if bmi < 16:
        result = 'Severe underweight'
    elif bmi < 18.5:
        result = 'Underweight'
    elif bmi < 25:
        result = 'Normal'
    elif bmi < 30:
        result = 'Overweight'
    else:
        result = 'Obese'
    posts = [bmi, result]

    return render_template('bmi.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
