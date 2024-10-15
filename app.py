from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello, world!")
    return "<p>Hello, World!</p>"

#https://python-kasa.readthedocs.io/en/latest/guides/light.html FOR TOMORROW
