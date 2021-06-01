import urllib.request
import os
import pathlib
import zipfile
from subprocess import Popen

openpose_download = "https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases/download/v1.6.0/openpose-1.6.0-binaries-win64-gpu-flir-3d_recommended.zip"

current_file_path = str(pathlib.Path().absolute())
openpose_install_path = current_file_path  + "/../build/openpose.zip"


########## INSTALL REQUIRED PYTHON MODULES ############

print("Installing required python modules")
os.system('pip install -r requirements.txt')

######### DOWNLOAD AND INSTALL OPENPOSE #################

print("Starting OpenPose download (418mb) - this may take a while")	
urllib.request.urlretrieve(openpose_download, openpose_install_path)										
print("OpenPose download complete")

print("Extracting openpose.zip")
with zipfile.ZipFile(openpose_install_path, 'r') as zip_ref:
    zip_ref.extractall(current_file_path  + "/../build")



print("Installing OpenPose - this may also take a while...")

os.chdir(current_file_path  + "/../build/openpose/models")
p = Popen("getModels.bat")
stdout, stderr = p.communicate()

print("OpenPose Installation completed")


