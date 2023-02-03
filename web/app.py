"""

Josh Muzi's Flask API.
"""
import os
import configparser
from flask import Flask, abort, send_from_directory, render_template


app = Flask(__name__)




@app.route("/<path:request>")
def hello(request):

	file_name = request

	if '..' in file_name or '~'	in file_name:


		return abort(403)

	file_path = os.path.join("pages/", file_name)
	print("File path: ", file_path)
	if os.path.isfile(file_path):

		return send_from_directory("pages/", file_name)
	else:

		return abort(404)
	return "UOCIS docker demo!\n"



@app.errorhandler(403)
def forbidden(e):
	return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def not_found(e):

	return send_from_directory('pages/', '404.html'), 404

def parse_config(config_paths):
	config_path = None
	for f in config_paths:
		if os.path.isfile(f):
			config_path = f
			break

	if config_path is None:
		raise RuntimeError("Configuration file not found!")

	config = configparser.ConfigParser()
	config.read(config_path)
	return config

config = parse_config(["credentials.ini", "default.ini"])
port_info = int(config["SERVER"]["PORT"])
debug_info = config["SERVER"]["DEBUG"].lower() == 'true'



if __name__ == "__main__":
	app.run(debug= debug_info, host='0.0.0.0', port = port_info)

