#
# This app wants to display phone's screen and intarct with it 
#

# -------------------
# Imports 
from adb_functions import *
from log_functions import *
import sys

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
# Display image

# -------------------
# Receive trigger from click on image

# -------------------
# Do the command on phone

# -------------------
# Goto first sub 



