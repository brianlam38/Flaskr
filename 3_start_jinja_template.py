#!/usr/bin/python

# import flask , url_forwarding, request, render_template modules
from flask import Flask, url_for, request, render_template
# create the app from the current file
app = Flask(__name__) # generate flask app from the name of the current file

# Flask will take in any web requests and process them through the functions that we write

# for any URL's stated by the path, call the following function
# NOTE: The hello_world() fn specifies what the page returns.
#		The @app.route() decator will let us change what the function does
#		A decator is a fn that takes in a fn and modifies how it behaves + returns it to be used like a normal fn
#		In this case, we are decorating the hello_world() fn to take in requests to the normal index page.

# base index
# get / post methods
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		return "Checking details..."
	else:
		return "Index"

@app.route("/hello")
def hello():
	return "Hello world!"

# user with username field -> get a specific username supplied by the user in the URL and return the username
# new route to add no user
@app.route("/user") # if no arg supplied, user will be set to None
@app.route("/user/<username>")
def profile(username=None):
	# template rendered should be in /templates
	return render_template("simple_hello.html", name=username)

@app.route("/debug")
def debug():
	# very long format html
	html = """
		<a href="{0}">{0}</a><br>
		<a href="{1}">{1}</a><br>
		<a href="{2}">{2}</a><br>
		<a href="{3}">{3}</a><br>
	""".format(
			# url_for() will give you back a link relative to where you currently are
			# useful if you are running a site that is dynamic to where its supposed to be
			# url_for() takes arg of a function name
			url_for("index"),
			url_for("hello"),
			# specify hello var = test
			url_for("hello", variable="test"),
			# specify username var = Quinn
			url_for("profile", username="Quinn")
			)
	return html

# if this program is being directly run
if __name__ == "__main__":
	# run the app, turn on debug + turn on reloader (instant reflect changes on website - edit on the go)
	app.run(debug=True, use_reloader=True)
	# alternate app.run() usage - we can also specify the port number
	# default port = 5000
	# app.run(debug=True, use_reloader=True, port=1531)



