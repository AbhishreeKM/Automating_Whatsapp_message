# importing the module
import pywhatkit

try:
    pywhatkit.sendwhatmsg("*********", "Happy birthday...hope all good for you", 00, 00)#phone number and message
    print("Successfully Sent!")
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")



