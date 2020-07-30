import os, json, random, flask
from flask import Flask

app = Flask(__name__)
@app.route('/')

def HelloWorld():
    return flask.render_template("index.html")
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)
