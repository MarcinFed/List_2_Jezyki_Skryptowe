import sys
import a
def print_all():
    for line in sys.stdin:
        try:
            print(line)
        except EOFError:
            break

if __name__ == "__main__":
    print_all()
    a.answer()