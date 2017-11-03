from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def basic():

    return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)
