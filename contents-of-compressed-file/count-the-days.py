#!/usr/bin/python

import datetime

#add your date to count down to. (year, month, day)
diff = datetime.datetime(2018, 11, 22) - datetime.datetime.today()
print diff.days +1,
