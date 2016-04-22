from adb_functions import *

ip = "10.100.105.153"
phone = uvp_phone()
out = phone.set_Phone_IP (ip)
if out == 1:
    print "Network Error"
    exit()
phone.adb_disconnect()
out = phone.adb_connect()
if out == 1:
    print "ADB connection error"
    exit()
out = phone.try_to_connect_if_offline()
if out == 1:
    print "Does't connect after 3 retries"
    exit()
phone.turn_off_dnd()
phone.adb_disconnect()
del phone