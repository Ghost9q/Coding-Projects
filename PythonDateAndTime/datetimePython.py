import datetime
date = datetime.date(2025, 6, 7)
today = datetime.date.today()
print(f'''
random date: {date}
todays's date: {today}
''')
time = datetime.time(12, 4, 5)
now = datetime.datetime.now()
print(f'''
random time: {time}
right now: {now}
''')
now_time = now.strftime('%H:%M:%S')
print(now_time)
now_date = now.strftime('%Y-%m-%d')
print(now_date)
# or you can print both date and time by combining the lines of code together.
# comparing two dates
target_datetime = datetime.datetime(2050,1,2,12,30)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print('Target date has passed.')
else:
    print('target date has NOT passed.')
    