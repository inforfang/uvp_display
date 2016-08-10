# uvp_display

## Remote intractive display for Executive Ubiquity phones using uvp_adb library
This is a sample project using uvp_adb library to connect to Ubiquiti (UVP) executive phone and 
intract with it. You can click on screen to intract with screen. 

Since it is using screenshots it is slow but it can be handy when you want to do remote 
assistance. 

## Usage : 
```shell
python uvp_display.py 1.2.3.4
```
* The last part is IP address 

## Requirements : 
* This script only tested to run on windows
* Uninstall PIL and Pillow libraries -> install Image (Which has both)
* Install adb 
* Install uvp_adb library 
