import sys
from tools import get_code
def only_200(lines):
    for line in lines:
        try:
            if get_code(line) == "200":
                print(line.strip())
        except:
            continue

if __name__=="__main__":
    only_200(sys.stdin)