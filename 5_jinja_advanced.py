#!/usr/bin/python

# IMPROVEMENT ON START.PY PROGRAM
# 
# This program includes GET / POST methods
# for a user to submit X+Y sum of two integers.

# import flask , url_forwarding, request, redirect modules
from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

# JINJA ADVANCED EXAMPLE
#
# base.html will be our default block. (see templates/base.html)
# "All our pages will have the title "Hello from Flask", with a main block after the title"
# This is useful as we can just specify all blocks of content in base.html if needed across all pages

# base index
# get / post methods
# instead of sending .html text, we are doing it via. render_template() function
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		# return the sum if they made a request
		try:
			z = int(request.form["x"]) + int(request.form["y"])
		except:
			z = 0
		return render_template("new_form.html", answer=z)
	else:
		# otherwise return a blank form
		return render_template("base.html", answer=None)

@app.route("/hello")
def hello():
	return "Hello world!"

# Re-directing to "hello" page.
# You can redirect to www.google.com or anything.
@app.route("/hi")
def hi():
	return redirect("hello")

# user with username field -> get a specific username supplied by the user in the URL and return the username
@app.route("/user")
@app.route("/user/<username>")
def profile(username=None):
	#users = {"Quinn": {"name": "Quinn", "degree": "Maths", "colour": "white"}}
	return render_template("hello.html", name=username)

@app.route("/debug")
def debug():
	# putting all URLs in a list format rather than html before
	data_list = [
		url_for("index"),
		url_for("hello"),
		url_for("hello", variable="test"),
		url_for("profile", username="Quinn")
		]
	return render_template("debug.html", data=data_list)

# if this program is being directly run
if __name__ == "__main__":
	# run the app, turn on debug + turn on reloader (instant reflect changes on website - edit on the go)
	app.run(debug=True, use_reloader=True)
	# alternate app.run() usage - we can also specify the port number
	# default port = 5000
	# app.run(debug=True, use_reloader=True, port=1531)



