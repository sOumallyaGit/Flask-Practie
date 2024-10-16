from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/Success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"    

    return render_template("result.html",result=res)


@app.route('/SuccessResults/<int:score>')
def SuccessResults(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"    

    exp = {"score":score,"res":res}    

    return render_template("resultAnother.html",result=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('SuccessResults',score=total_score))

if __name__=="__main__":
    app.run(debug=True)