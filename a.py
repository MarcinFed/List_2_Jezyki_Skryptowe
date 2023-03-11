import sys
from tools import get_code

def answer_codes(lines):
    count_200=0
    count_302=0
    count_404=0
    for line in lines:
        try:
            code = get_code(line)
            if code == "200":
                count_200+=1
            elif code == "302":
                count_302+=1
            elif code == "404":
                count_404+=1
        except ValueError:
            continue
    return [count_200, count_302, count_404]

def answer():
    result = answer_codes(sys.stdin)
    sys.stdin.close()
    print(f"200: {result[0]}")
    print(f"302: {result[1]}")
    print(f"404: {result[2]}")


if __name__=="__main__":
    answer()

