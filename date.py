from datetime import datetime

today = datetime.today()
print("Today's date is", today)

today = datetime.today() 
 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

today = datetime.today() 
 
print("Current hour:", today.hour)
print("Current minute:", today.minute)
print("Current second:", today.second)

now=datetime.now()
print("current date :", now)

# date_str='2024-10-1 12:50:10'
# date_form = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
# print("string to date-time: ",date_form)

# date_bday=datetime(2003,9,13)

# time_diff = datetime.now()-date_bday
# print("time difference: ", time_diff)


date_bday=input("enter date in this format yyyy-mm-dd: ")

time_diff = datetime.now()-date_bday
print("time difference: ", time_diff)