from flask import Flask, render_template
app = Flask(__name__) # tạo server

# tên route và hàm phải khác nhau
@app.route('/')
def index():
    posts =[
        {
            'title':"Thơ",
            'author':"Chung",
            'content':"CHUNG",
            'gender':1
        },
        {
            'title':"Thơ",
            'author':"Yến",
            'content':"YẾN",
            'gender':0
        }
    ]
    # return '<p><span style="text-decoration: underline;"><em><strong>hello world</strong></em></span></p>'
    # return render_template("index.html",post_title=title,author=author,post_content=content)
    return render_template("index.html",posts=posts)
    # để tên biến giống tên của dict cũng đc
    # hàm vào thư mục templates tìm file giống
@app.route ("/c4e") # bắt đầu luôn là /
def sayhi():
    return 'HI'

@app.route ("/hi/<name>/<age>") # bắt đầu luôn là /
def sayhi1(name,age):
    return '<p><span style="text-decoration: underline;"><em><strong>Hi {0}. You are {1} years old</strong></em></span></p>'.format(name,age)
# <name> giống trong chỗ def sayhi1(name)
# <> là request parameter thì trong hàm phải có parameter đó

#return luôn trả về string
# @app.route ("/sum/<a>/<b>")
# def s(a,b):
#     return str(int(a)+int(b))
@app.route ("/sum/<int:a>/<int:b>")
def s(a,b):
    return str(a+b)

if __name__ == '__main__':
  app.run(debug=True)
