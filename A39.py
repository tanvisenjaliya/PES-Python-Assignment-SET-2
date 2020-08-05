import time
localtime = time.asctime(time.localtime(time.time()))
print ("Local current time :", localtime)

import calendar
cal = calendar.month(2020,4)
print ("\nHere is the calendar:")
print (cal)
