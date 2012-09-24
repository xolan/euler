#!/bin/env python

import datetime

sundays = 0
for y in range(1901, 2001, 1):
    for m in range(1, 13, 1):
        if datetime.date(y, m, 1).weekday() == 6:
            sundays += 1

print(sundays)
