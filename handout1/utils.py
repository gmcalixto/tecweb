import json
from pathlib import Path

def extract_route(request):
    if (request.splitlines()[0])[0:4] == 'POST':
        return (request.splitlines()[0])[6:-9]
    else:
        return (request.splitlines()[0])[5:-9]


def read_file(filepath):   
    f = open(filepath, 'rb')
    return f.read()


def load_data(file):
    with open('data/' + file, "r") as read_file:
        data = json.load(read_file)
        return data

def write_json(file,content):   
    data = load_data(file)
    data.append(content)
    
    with open('data/' + file, 'w') as outfile:
        json.dump(data, outfile)


def load_template(file):
    with open('templates/' + file, "r") as read_file:
        return read_file.read()

def build_response(body='', code=200, reason='OK', headers=''):
    return ('HTTP/1.1 ' + str(code) + ' ' + reason  + '\n\n').encode()

