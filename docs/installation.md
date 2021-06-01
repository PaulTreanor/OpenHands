
:warning: The installation process isn't fully tested and might not fully work. 

# Installing OpenHands 

## System requirements (version 0.1.0)
-   Windows 10 64-bit
-   NVidia GPU with at least 2GB of RAM

## Dependencies 
#### Python
-   Supports version 3.6 or later
-   Download from  [https://www.python.org](https://www.python.org).

## System download 
Download and extract the project's [github repository](https://github.com/PaulTreanor/openhands).

## API installation 
To install the classification API run the following command from within the repository's /res directory:

```
python server_install.py
```

This will run a script which downloads and installs OpenPose in the correct location, and install required python modules.

## Running the server 
To start an Jester API server run the following command from the classifier folder:

```
python flask_server.py
```