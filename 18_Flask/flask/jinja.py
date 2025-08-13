# building URL Dynamically
# Variable Rule
# Jinja 2 Template Engine

from flask import Flask, render_template, request, redirect, url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask app. Debug = true."

@app.route("/html")
def html():
    return "<html> <h1>this is an html page with H1 tag.</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


## variable rule
@app.route('/success/<int:score>')
def succcess(score):
    # return "The marks you got is "+ str(score)
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

### jinja2 template engine
    return render_template('result.html', results=res)


@app.route('/successres/<int:score>')
def successres(score):
    # return "The marks you got is "+ str(score)
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

### jinja2 template engine
    exp={'score':score, 'res':res}
    return render_template('result1.html', results=exp)

@app.route('/successif/<int:score>')
def succcessif(score):
    return render_template('result.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        datascience=float(request.form['datascience'])
        c=float(request.form['c'])
        total_score = (science + maths + datascience + c)/4
        return redirect(url_for('successres', score=total_score)) ## dynamic url
    return render_template('getresults.html')


if __name__ == "__main__":
    app.run(debug=True)