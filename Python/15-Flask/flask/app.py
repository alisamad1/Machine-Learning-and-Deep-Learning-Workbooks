from flask import Flask 
'''
It creates an instance of the flask class,
which will be your WSGI(Web server Gateway Interface) application.
'''
## WSGI Application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to this flask course. this should be an nice amazing course"
@app.route("/index")
def Safety():
    return "You are not safe if you are in Kashmir"
if __name__ == "__main__":
    app.run(debug=True)