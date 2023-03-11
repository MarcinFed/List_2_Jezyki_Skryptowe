import re

def process_line(line):
    try:
        data = re.match(r"(.+) - - \[(.+) \"(.+)\" (.+) (.+)", line)
        return [data[1], data[2], data[3], data[4], data[5]]
    except:
        raise Exception("Wrong data!")

def get_code(line):
    code = process_line(line)
    return code[3]

def get_bytes(line):
    bytes = process_line(line)
    return bytes[4]

def get_request(line):
    request = process_line(line)
    return request[2]

def get_path(line):
    request = get_request(line)
    splited = request.split()
    if len(splited) < 2:
        return request
    return splited[1].strip()

def get_date(line):
    date = process_line(line)
    return date[1]

def get_host(line):
    host = process_line(line)
    return host[0]

def filtered_print(file, filter):
    for line in file:
        if filter(line):
            print(line.strip())
    file.close()