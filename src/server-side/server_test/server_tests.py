import os
import requests
import pytest 
import socket
import pathlib

LOCAL_IP_ADDRESS = socket.gethostbyname(socket.gethostname())
API_URL = 'http://'+LOCAL_IP_ADDRESS+':5000/'

test_image_folder_path = str(pathlib.Path().absolute())

# Status codes 
OK_STATUS_CODE = 200
SUCCESS_STATUS_CODE = 201
FILETYPE_ERROR_STATUS_CODE = 422

def post_file(filename, filepath="./"):
	files = {'file': open(filepath+filename, 'rb')}
	response = requests.post(API_URL + filename, files=files)
	print(response.status_code)
	print(response.text)
	return response

def test_connection():
	response = requests.get(API_URL)
	assert response.status_code == OK_STATUS_CODE

def test_ood_image():
	filepath = test_image_folder_path + "/test-images/ood/"
	filename = 'image.jpg'
	response = post_file(filename, filepath)
	assert response.status_code == SUCCESS_STATUS_CODE and response.text == "OOD"


def test_gesture_image():
	filepath = test_image_folder_path + "/test-images/alt-palm/"
	filename = 'image.jpg'
	response = post_file(filename, filepath)
	assert response.status_code == SUCCESS_STATUS_CODE and response.text == "palm"

def test_400_error():
	filename = 'test_text.txt'
	response = post_file(filename)
	assert response.status_code == FILETYPE_ERROR_STATUS_CODE

if __name__ == "__main__":
	# Test connection
	response = requests.get(API_URL)
	print(response.status_code, response.text)
	# Send file
	filepath = test_image_folder_path + "/test-images/alt-palm/"
	filename = 'image.jpg'
	post_file(filename, filepath)

