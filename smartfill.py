import datetime

def getWeekNumber():
    start = datetime.date(2019, 8, 26)
    week = datetime.timedelta(weeks = 1)
    delta = datetime.date.today() - start

    # If delta is less than week * i then i is the week
    for i in range(1, 17):
        if delta < week * i:
            return i - 1

print(getWeekNumber())