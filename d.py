import sys
from tools import get_path
def data_ratio(lines):
    graphic_data = 0
    other_data = 0
    for line in lines:
        try:
            file_extension=get_path(line).split(".")
            if len(file_extension) >1:
                extension = file_extension[1].strip()
                if extension =="gif" or extension == "jpg" or extension == "jpeg" or extension == "xbm":
                    graphic_data +=1
                else:
                    other_data+=1
        except:
            continue
    return graphic_data/(other_data+graphic_data)

def answer():
    result = data_ratio(sys.stdin)
    sys.stdin.close()
    print(f"Stosunek pobrań zasobów graficznych do pozostałych jest równy: {result:.2f}")

if __name__=="__main__":
    answer()
