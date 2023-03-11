import datetime
import sys
from tools import get_date


def between_22_6(lines):
    for line in lines:
        try:
            date = get_date(line).split()[0]
            time = datetime.datetime.strptime(date, "%d/%b/%Y:%H:%M:%S")
            if time.hour >=22 or time.hour<6:
                print(line.strip())
        except:
            continue

if __name__=="__main__":
    between_22_6(sys.stdin)
