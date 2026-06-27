        #DAY 15
import time

time=input("Enter the time in hours, minutes and seconds (HH:MM:SS): ")

if (time>="00:00:00" and time<="11:59:59"):
    print("Good Morning")
elif (time>="12:00:00" and time<="15:59:59"):
    print("Good Afternoon")
elif (time>="16:00:00" and time<="20:59:59"):
    print("Good Evening")
else:
    print("Good night")

# current_time=time.strftime('%H:%M:%S')
# print("Thank for mentioning the time here is the Current IST[Indian Standard Time]",current_time)

# timestrap = time.strftime('%H:%M:%S')
# print("Current Time =", timestrap)

# date=time.strftime('%Y-%m-%d %H:%M:%S')
# print("Current Date and Time =", date)




                    #Checked this on day 26 and it's right