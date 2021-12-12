import datetime

print(dir(datetime))
# class - date, time, datetime

# print(help(datetime.date))

dob = datetime.date(1974, 3, 21)
print("dob", dob)
print("dob.year", dob.year)  # or month or day

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)  # 100 days
print(mill + dt)  # 100 days after mill

print("\n String formatting")
print(dob.strftime("%A, %B %d, %Y"))
message = "Born on {:%A, %B %d, %Y}."
print(message.format(dob))

print("\nLaunch date tests")
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3,30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)
print(launch_time.hour)

print("\n")
now = datetime.datetime.today()
print("now", now)
print("now.microsecond", now.microsecond)

print("\nMoon landing date conversion")
moon_landing = '7/20/1969'
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))
