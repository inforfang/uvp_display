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
The last part is IP address 

## Requirements : 
You need to install uvp_adb first for this to work. It also work in both windows and linux. I 
mostly tested it in Windows envoirement but I tried with Lubuntu distro and it worked fine. 

For linux you need to have graphical interface to use it. It uses PIL and Tkinter libraries too 
for displaying the shot. 
