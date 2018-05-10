from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    posts ={
            'name':"Trần Ngọc Bảo Chung",
            'DOB':"30/11/1997",
            'school':"Đại học Bách Khoa Hà Nội"
            }
    return render_template('info.html',posts=posts)

@app.route('/school')
def school():
    return redirect('http://techkids.vn ', code=302)

if __name__ == '__main__':
  app.run(debug=True)
