#!/usr/bin/python

# import flask module
from flask import flask
# create the app from the current file
app = Flask(__name__) # generate flask app from the name of the current file

# Flask will take in any web requests and process them through the functions that we write

# for any URL's stated by the path, call the following function
@app.route("/")
def hello_world():
	return "Hello world!"

# if this program is being directly run
if __name__ == "__main__":
	# run the app, turn on debug + turn on reloader (instant reflect changes on website - edit on the go)
	app.run(debug=True, use_reloader=True)
	# alternate app.run() usage - we can also specify the port number
	# default port = 5000
	# app.run(debug=True, use_reloader=True, port=1531)



