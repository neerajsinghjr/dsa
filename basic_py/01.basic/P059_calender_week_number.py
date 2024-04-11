import datetime

today = datetime.datetime.today()
print("today: ", today)
week_num = today.isocalendar()[1]

print("Week Number:", week_num, "Weeks")