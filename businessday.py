import datetime
import holidays

'''
find last/next business day
'''

def last_business_day(date):
    last_day = date-datetime.timedelta(days=1)
    while last_day.weekday() in holidays.WEEKEND or last_day in holidays.US():
        last_day-=datetime.timedelta(days=1)
    return last_day
    
def next_busuness_day(date):
    next_day = date+datetime.timedelta(days=1)
    while next_day.weekday() in holidays.WEEKEND or next_day in holidays.US():
        next_day+=datetime.timedelta(days=1)
