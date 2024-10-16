from flask import Flask

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

app=Flask(__name__)

@app.route("/")
def welcomepage():
    return "Hello To My First Flask Page"

@app.route("/index")
def index():
    return "Welcome To the Index page"

if __name__=="__main__":
    app.run()