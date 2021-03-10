from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/human/<human>/<int:id>')
def human(human=None, id=None):
    return render_template("human.html", human=human, id=id)


@app.route('/about')
def blog():
    return render_template("about.html")
