# app.py
# pip install flask
# pip install flask-mysql

from flask import *
from models import hash_convert

app = Flask(__name__)


# http://127.0.0.1:5000/first
@app.route("/first")
def first():
    return render_template('first.html')

#http://127.0.0.1:5000/hash
@app.route("/hash", methods = ['GET'])
def hash():
    user_txt = request.args.get('usr_txt')
    user_img = request.args.get('usr_img')
    result = hash_convert.np2hash(hash_convert.pixel_list(user_img), user_txt)
    return render_template('first.html', hash_val = result)

if __name__ == '__main__':
    app.debug = True
    app.run()
