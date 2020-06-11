from flask import Flask

# do this every time, instantiate a new application object! Now a server is made.
app = Flask(__name__)


@app.route("/welcome")
def welcome():
    html = "<html><body><h1>welcome</h1></body></html>"
    return html


@app.route('/welcome/home')
def welcome_home():
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html


@app.route('/welcome/back')
def welcome_back():
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html
