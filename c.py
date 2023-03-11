import sys
from tools import get_bytes, get_path

def largest_resource(lines):
    largest_resource_size = 0
    largest_resource_path = ""
    for line in lines:
        try:
            resource_size = int(get_bytes(line))
            resource_path = get_path(line)
            if resource_size>largest_resource_size:
                largest_resource_size=resource_size
                largest_resource_path=resource_path
        except:
            pass
    return [largest_resource_path, largest_resource_size]

def answer():
    result = largest_resource(sys.stdin)
    sys.stdin.close()
    print(f"Największy zasób: {result[0]} ({result[1]} bajtów)")


if __name__ == "__main__":
    answer()