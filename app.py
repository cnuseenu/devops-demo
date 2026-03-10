from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "DevOps CI/CD Demo Running!"

app.run(host="0.0.0.0", port=5000)
