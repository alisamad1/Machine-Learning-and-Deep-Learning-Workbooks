from flask import Flask,render_template
'''
It creates an instance of the flask class,
which will be your WSGI(Web server Gateway Interface) application.
'''
## WSGI Application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1> Welcome to the flask course<H1></html>"
@app.route("/index")
def Safety():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)