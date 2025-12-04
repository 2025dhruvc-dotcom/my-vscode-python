import datetime
now=datetime.datetime.now()
print(now)
today=datetime.date.today()
print(today)

d = datetime.date(2025,12,1)
print(d.strftime("%y/%m/%d"))