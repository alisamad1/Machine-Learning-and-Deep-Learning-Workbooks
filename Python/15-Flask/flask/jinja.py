# this  is our first tutorial for our jinja
##  building URL Dynamically
# jinja 2 template engine
'''
{{  }} expression to print output in html
{%.....%} conditions, for loops
{#.....#} to write comments
'''
from flask import Flask, render_template, request
'''
It creates an instance of the flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''
## WSGI Application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask course</h1></html>"
@app.route("/index", methods=['GET'])
def Safety():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f" Hello{name}"
    return render_template("form.html")
@app.route('/submit', methods = ['GET', "POST"])
def submit():
    if request.method == "POST":
        name = request.form['name']
        return f'Hello  Bhai {name}!'
    return render_template('form.html')
## variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res="pass"
    else:
        res = 'fail' 
    return render_template('results.html',results = res)
## variable rule
@app.route('/exam/<int:score>')
def successor(score):
    res = ""
    if score >= 50:
        res="pass"
    else:
        res = 'fail' 
    exp={'score':score, "res" : res}
    return render_template('result_1.html',results = res)
@app.route('/sucessessexample/<int:score>')
def kayhuaresult(score):
    res = ""
    if score >= 50:
        res="pass"
    else:
        res = 'fail' 
    exp={'score':score, "res" : res}
    return render_template('result_1.html',results = res)
if __name__ == "__main__":
    app.run(debug=True)
