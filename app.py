from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/plot/")
def plot():
    return render_template('plot.html')

@app.route("/the_seven/")
def the_seven():
    return render_template('the_seven.html')

@app.route("/stats/")
def stats():
    return render_template('stats.html')

@app.route("/cool_facts/")
def cool_facts():
    return render_template('cool_facts.html')

if __name__ == "__main__":
    app.run()
