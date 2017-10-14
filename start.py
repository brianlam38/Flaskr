#!/usr/bin/python

# import flask module
from flask import flask
# create the app from the current file
app = Flask(__name__) # generate flask app from the name of the current file

# Flask will take in any web requests and process them through the functions that we write

# for any URL's stated by the path, call the following function
# NOTE: The hello_world() fn specifies what the page returns.
#		The @app.route() decator will let us change what the function does
#		A decator is a fn that takes in a fn and modifies how it behaves + returns it to be used like a normal fn
#		In this case, we are decorating the hello_world() fn to take in requests to the normal index page.

# base level
@app.route("\n")
def index():
	rturn "Index"

@app.route("/hello")
def hello():
	return "Hello world!"

# user with username field -> get a specific username supplied by the user in the URL and return the username
@app.route("/user/<username>")
def profile(username):
	return "Hello {}".format(username)

# if this program is being directly run
if __name__ == "__main__":
	# run the app, turn on debug + turn on reloader (instant reflect changes on website - edit on the go)
	app.run(debug=True, use_reloader=True)
	# alternate app.run() usage - we can also specify the port number
	# default port = 5000
	# app.run(debug=True, use_reloader=True, port=1531)



