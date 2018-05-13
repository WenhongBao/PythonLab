import re 
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    cday=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    return cday.timestamp()

t1=to_timestamp('2015-6-1 08:10:30','UTC+7:00')
assert t1==1433121030.0,t1

t2=to_timestamp('2015-5-31 16:10:30','UTC-9:00')
assert t2==1433121030.0,t2

print('pass')