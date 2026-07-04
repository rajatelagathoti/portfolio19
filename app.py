from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
  return open("YouTube.html").read()
app.run(debug = "True")
