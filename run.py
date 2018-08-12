from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
        data = [list(d) for d in data]
        t_b = [d.pop(0) for d in data]
        d = zip(t_b,data)
    except Exception as e:
        print e
        data = None
    return render_template("home.html", data=d)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
