import datetime
import sys
from tools import get_date

def only_from_friday(lines):
    for line in lines:
        try:
            date = get_date(line).split()[0]
            proper_date = datetime.datetime.strptime(date, "%d/%b/%Y:%H:%M:%S")
            if proper_date.weekday()==4:
                print(line.strip())
        except:
            continue

if __name__=="__main__":
    only_from_friday(sys.stdin)