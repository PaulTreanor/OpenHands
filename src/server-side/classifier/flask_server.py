import os
import time
from flask import Flask, request, abort
from get_class import getClass
from flask_cors import CORS
import pathlib

api = Flask(__name__)
CORS(api)		# Ignores any CORS issues 
import configparser
# Read image upload path from jester.ini
config = configparser.ConfigParser()
config.read('jester.ini')
current_file_path = str(pathlib.Path().absolute())

root_upload_path = current_file_path + '/uploads'

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', ""}



@api.route("/<filename>", methods=["POST"])
def post_file(filename):

	if 'file' not in request.files:
			return "File didn't send", 404

	# Create new directory for each request (OpenPose only reads images)
	filename, fileExtension = os.path.splitext(filename)
	print(fileExtension)
	if fileExtension not in ALLOWED_EXTENSIONS:
		return "Invalid filetype", 422
	os.mkdir(current_file_path + '/uploads')
	upload_path = root_upload_path + '/' + filename	
	os.mkdir(upload_path)

	file = request.files['file']
	file.save(upload_path +'/image.jpg')
	classification = getClass(upload_path)

	# Delete directory
	os.rmdir(upload_path)
	os.rmdir(current_file_path + '/uploads')
	# 201 - created 
	return classification, 201

@api.route("/")
def test_connection():
	return "Connection OK", 200

if __name__ == "__main__":
	api.run(host='0.0.0.0', debug=True, port=5000)