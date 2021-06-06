



:warning: The installation process isn't fully tested.


# Installing OpenHands 

## System requirements (version 0.1.0)
-   NVidia GPU with at least 2GB of RAM

## Dependencies 
- Python 3.6 or later
## System download 
Download and extract the project's [github repository](https://github.com/PaulTreanor/openhands).

## Installation 

### Windows
Run `python server_install.py` from within the repository's `/scripts` directory:

This will run a script which downloads and installs OpenPose in the correct location, and install required python modules.

### Linux 

1. Install the required Python modules by running `pip install -r requirements.txt` from the `/scripts` directory.
3. Download and install [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md) into the `/build` directory. 




### Verify OpenPose Installation
The system is dependent on OpenPose, which can throw "out of memory" errors depending on hardware/software environemnts, even when the OpenPose hardware requirements are met. It also has a vast amount of dependencies which are difficult to install manually. For these reasons the OpenPose installation should be verified, if it was installed via the Windows script. 

Test the installation by CDing to the root of the OpenPose directory (which should be `/build/OpenPose`) and run one of following commands:
```
# Linux - manual OpenPose install
./build/examples/openpose/openpose.bin
```

```
# Windows - install script
bin\OpenPoseDemo.exe --video examples\media\video.avi
```
If OpenPose successfully runs then OpenHands should be successfully installed. 

## Running the server 
To start an API serving OpenHands run the following command from the classifier folder:

```
python flask_server.py
```