from flask import *
from mongoengine import *
import mlab
from models.ytube import ytube
from youtube_dl import YoutubeDL
app = Flask(__name__)
# chech session
app.secret_key = "123456789"
mlab.connect()

@app.route('/')
def index():
    videos = ytube.objects()
    return render_template('index.html',videos=videos)

@app.route('/detail/<youtubeid>')
def detail(youtubeid):
    return render_template('detail.html',youtubeid=youtubeid)

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for("admin"))
        else:
            return "error"
@app.route('/logout')
def logout():
    if 'loggedin' in session:
        del session['loggedin']
        return redirect(url_for("index"))
    else:
        return 'error'

@app.route('/admin', methods=["GET","POST"])
def admin():
    if "loggedin" in session:
        if request.method == "GET":
            videos = ytube.objects()
            return render_template('admin.html', videos=videos)
        elif request.method == "POST":
            form=request.form
            link=form['link']
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download=False)
            title =  data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtubeid = data['id']
            video = ytube(  title=title,
                            thumbnail = thumbnail,
                            views=views,
                            youtubeid=youtubeid,
                            link=link)
            video.save()
            return redirect(url_for("admin"))
    else:
        return redirect(url_for("login"))



if __name__ == '__main__':
  app.run( debug=True)
