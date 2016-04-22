#
# This app wants to display phone's screen and intarct with it 
#

# -------------------
# Imports 
from adb_functions import *
from log_functions import *
import sys
import time

# -------------------
# take ip 
if len(sys.argv) < 2 :
    print '\nUsage   :  UVPDisplay.py  <phone-ip-address> \
           \nExample :  UVPDisplay.py  10.100.105.136\n'
    sys.exit(1)

PHONE_IP = str(sys.argv[1])

def take_screen_shot(ip):
    phone = uvp_phone()
    out = phone.set_Phone_IP (ip)
    if out == 1: 
        return 1    #in case of network error
    phone.adb_disconnect()
    out = phone.adb_connect()
    if out == 1:
        return 1    #in case of connection to phone error 
    out = phone.try_to_connect_if_offline()
    if out == 1:
        return 1    #in case of can't connect to phone after retries error 
    
    phone.take_screenshot()
    
    phone.adb_disconnect()
    del phone
    return 0


# -------------------
# Take an screenshot 
take_screen_shot(PHONE_IP)


# -------------------
# Do the command on phone
def adb_click(event):
    #outputting x and y coords to console
    phone = uvp_phone()
    out = phone.set_Phone_IP (PHONE_IP)
    if out == 1: 
        return 1    #in case of network error
    phone.adb_disconnect()
    out = phone.adb_connect()
    if out == 1:
        return 1    #in case of connection to phone error 
    out = phone.try_to_connect_if_offline()
    if out == 1:
        return 1    #in case of can't connect to phone after retries error 
    
    phone._adb_run_shell_command ("adb shell input tap "+str(event.x)+" "+str(event.y))
    
    phone.adb_disconnect()
    del phone
    time.sleep (4)
    
    take_screen_shot(PHONE_IP)
    img = ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))
    return 0
    
# -------------------
# Display image
from Tkinter import *
from PIL import Image, ImageTk
#pip remove pillow
#pip install image 

root = Tk()

#setting up a tkinter canvas with scrollbars
frame = Frame(root, bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=1, column=0, sticky=E+W)
yscroll = Scrollbar(frame)
yscroll.grid(row=0, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
xscroll.config(command=canvas.xview)
yscroll.config(command=canvas.yview)
frame.pack(fill=BOTH,expand=1)

#adding the image
image = Image.open("screen.png")
img = ImageTk.PhotoImage(image)

canvas.create_image(0,0,image=img,anchor="nw")
canvas.config(scrollregion=canvas.bbox(ALL))

# -------------------
# Receive trigger from click on image
#mouseclick event
#function to be called when mouse is clicked
canvas.bind("<Button 1>",adb_click)
root.mainloop()