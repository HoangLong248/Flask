from flask import Flask, request, make_response, redirect, abort


app = Flask(__name__)

@app.route("/")
def index():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie('answer', '42')
    return response

@app.route("/redirect")
def redirect_index():
    return redirect("https://google.com.vn")

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, %s" % name

@app.route("/user/<name>")
def get_user(name):
    print(name)
    if not name:
        abort(404)
    return '<h1>Hello, %s' % name

if __name__ == "__main__":
    app.run(debug=True)