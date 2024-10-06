from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "THis is the DNS TakeOver POC by muhammadIlyas(https://hackerone.com/muhammadilyas)"
