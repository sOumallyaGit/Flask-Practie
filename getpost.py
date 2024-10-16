from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home route"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)