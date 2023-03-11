import sys
from tools import get_bytes

def calculate_data(lines):
    byte_count = 0
    for line in lines:
        try:
            byte_count+=int(get_bytes(line))
        except ValueError:
            continue
    giga = byte_count / 1024 / 1024 / 1024
    return giga

def answer():
    result=calculate_data(sys.stdin)
    sys.stdin.close()
    print(f"Sumaryczna liczba danych wysłanych do hostów: {result:.2f} GB")

if __name__=="__main__":
    answer()