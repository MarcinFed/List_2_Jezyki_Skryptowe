import sys
from tools import get_host

def only_poland(lines):
    for line in lines:
        try:
            domain=get_host(line).split(".")[-1]
            if domain == "pl":
                print(line.strip())
        except:
            continue

if __name__=="__main__":
    only_poland(sys.stdin)