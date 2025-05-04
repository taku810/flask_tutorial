#render_template：HTMLを表示させる関数
from flask import Flask, render_template, request, redirect, url_for
from models.models import OnegaiContent
from models.database import db_session
from datetime import datetime

#flaskオブジェクトの作成
app = Flask(__name__)

#「/home」にアクセスがあったときに「index.html」を返す
@app.route("/home")
def home():
    name = request.args.get("name")
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name = name, all_onegai = all_onegai)

@app.route("/home", methods=["post"])
def post():
    name = request.form["name"]
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name = name, all_onegai = all_onegai)

@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title, body, datetime.now())
    db_session.add(content)
    db_session.commit()
    return redirect(url_for('home'))

@app.route("/update", methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()

@app.route("/delete", methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

@app.route("/")
def index():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)