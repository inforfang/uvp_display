# ===========================================
# UVPDisplay.py
#
# Shows phone's screen and you can click and interact with it !!!
# Note : Run in windows / uninstall PIL and Pillow / install Image (Which has both)
#
# ===========================================

# -------------------
# Imports 
from uvp_adb import *
import sys
import time

logg = uvp_log()
logg.set_show_on_screen(True)
logg.set_write_to_file(False)
logg.set_tag ("DISPLAY")
logg.set_log_filename ("uvp_display.log")

# -------------------
# take ip 
if len(sys.argv) < 2 :
    print '\nUsage   :  UVPDisplay.py  <phone-ip-address> \
           \nExample :  UVPDisplay.py  10.100.105.136\n'
    sys.exit(1)

PHONE_IP = str(sys.argv[1])

def take_screen_shot(ip):
    phone = uvp_phone()

    phone.uvp_log.set_show_on_screen(True)
    #phone.uvp_log.set_log_filename = "uvp_display.log"

    out = phone.set_Phone_IP (ip)
    if out == 1:
        phone.uvp_log.error ("Network Error")
        return 1    #in case of network error
    phone.adb_disconnect()
    out = phone.adb_connect()
    if out == 1:
        phone.uvp_log.error ("ADB connection error")
        return 1    #in case of connection to phone error 
    out = phone.try_to_connect_if_offline()
    if out == 1:
        phone.uvp_log.error ("Does't connect after 3 retries")
        return 1    #in case of can't connect to phone after retries error 
    
    phone.take_screenshot()
    logg.info ("Screenshot has been taken")
    phone.adb_disconnect()
    del phone
    return 0

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
    
    phone._adb_run_shell_command ("adb shell input tap "+str(event.x)+" "+str(event.y), True)
    logg.info ("Click coordinates : "+ str(event.x)+" , "+str(event.y))
    phone.adb_disconnect()
    del phone
    #time.sleep (4)
    
    take_screen_shot(PHONE_IP)
    global image,img,canvas
    image = Image.open("screen.png")
    img = ImageTk.PhotoImage(image)

    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))
    return 0
  
  
  

# -------------------
# Take an screenshot 
if take_screen_shot(PHONE_IP) == 1:
    print "Error"
    exit()

    
# -------------------
# Display image
logg.info ("uvp_display app started!")
from Tkinter import *
from PIL import Image, ImageTk
#pip remove pillow
#pip install image 

root = Tk()

#setting up a tkinter canvas with scrollbars
frame = Frame(root, bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
#xscroll = Scrollbar(frame, orient=HORIZONTAL)
#xscroll.grid(row=1, column=0, sticky=E+W)
#yscroll = Scrollbar(frame)
#yscroll.grid(row=0, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
#xscroll.config(command=canvas.xview)
#yscroll.config(command=canvas.yview)
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
