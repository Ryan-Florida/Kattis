from sys import stdin
from calendar import weekday

wd = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday', 3 : 'Thursday', 4 :
'Friday', 5 : 'Saturday', 6 : 'Sunday'}

for line in stdin:
    print(wd[weekday(2009, int(line.split()[1]), int(line.split()[0]))])
