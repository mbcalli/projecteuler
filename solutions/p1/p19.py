import datetime

start = datetime.datetime.strptime("01-01-1901", "%d-%m-%Y")
end = datetime.datetime.strptime("31-12-2000", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dates = [x for x in date_generated if x.weekday() == 6 and x.day == 1]

print(len(dates))