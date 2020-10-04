from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/departures/')
def departures():
    return render_template('departure.html')


@app.route('/tours/')
def tours():
    return render_template('tour.html')


app.run()
