from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/user/<username>')

def index(username):
    users = {
            'huy':  {
                    'name': 'Nguyễn Quang Huy',
                    'age': 29,
                    'gender': 'nam'
            },
            'don':  {
                    'name': 'Phạm Quý Đôn',
                    'age': 22,
                    'gender': 'nam'
            },
            'quan':{
                    'name': 'Nguyễn Anh Quân',
                    'age': 22,
                    'gender': 'nam'
            },
            'anh': {
                    'name': 'Huỳnh Tuấn Anh',
                    'age': 23,
                    'gender': 'nam'
            }
    }
    if username in users.keys():
        post = users[username]
        return render_template('info2.html', post = post)
    else:
        return 'User not found'

if __name__ == '__main__':
    app.run(debug=True)
