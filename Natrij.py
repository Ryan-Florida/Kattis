from sys import stdin
from datetime import datetime
cur                = stdin.readline().rstrip('\n')
ex                 = stdin.readline().rstrip('\n')
FMT                = "%H:%M:%S"
timeUntilExplosion = datetime.strptime(ex,FMT) - datetime.strptime(cur,FMT)
tue = str(timeUntilExplosion)
if('day' in tue):
    print('%02d:%02d:%02d' %(int(tue.split(',')[1].split(':')[0]),int(tue.split(',')[1].split(':')[1]),int(tue.split(',')[1].split(':')[2])))
else:
    print('%02d:%02d:%02d' %(int(tue.split(':')[0]),int(tue.split(':')[1]),int(tue.split(':')[2])))
