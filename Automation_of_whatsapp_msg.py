# importing the module
import pywhatkit

try:
	list=["*********","*********","*********"] /#phone numbers to send message
	j=33

	for i in list:
	
		pywhatkit.sendwhatmsg(i, "Hi this msg is auto generated", 17, j)
		j=j+5

	print("Successfully Sent!")
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")



