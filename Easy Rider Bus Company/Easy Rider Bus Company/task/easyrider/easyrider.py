import itertools
from datetime import timedelta
import json


def test_1():
    # On demand stops test:
    # Wrong stop type: ['Abbey Road', 'Elm Street']
    return '[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "O", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 7, "stop_type" : "O", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]'


def test_3():
    # On demand stops test:
    # Wrong stop type: ['Sunset Boulevard']
    return '[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]'


def input_1():  #
    # On demand stops test:
    # Wrong stop type: ['Elm Street', 'Sunset Boulevard']
    return '''
                [
                    {
                        "bus_id": 128,
                        "stop_id": 1,
                        "stop_name": "Prospekt Avenue",
                        "next_stop": 3,
                        "stop_type": "S",
                        "a_time": "08:12"
                    },
                    {
                        "bus_id": 128,
                        "stop_id": 3,
                        "stop_name": "Elm Street",
                        "next_stop": 5,
                        "stop_type": "O",
                        "a_time": "08:19"
                    },
                    {
                        "bus_id": 128,
                        "stop_id": 5,
                        "stop_name": "Fifth Avenue",
                        "next_stop": 7,
                        "stop_type": "O",
                        "a_time": "08:25"
                    },
                    {
                        "bus_id": 128,
                        "stop_id": 7,
                        "stop_name": "Sesame Street",
                        "next_stop": 0,
                        "stop_type": "F",
                        "a_time": "08:37"
                    },
                    {
                        "bus_id": 256,
                        "stop_id": 2,
                        "stop_name": "Pilotow Street",
                        "next_stop": 3,
                        "stop_type": "S",
                        "a_time": "09:20"
                    },
                    {
                        "bus_id": 256,
                        "stop_id": 3,
                        "stop_name": "Elm Street",
                        "next_stop": 6,
                        "stop_type": "",
                        "a_time": "09:45"
                    },
                    {
                        "bus_id": 256,
                        "stop_id": 6,
                        "stop_name": "Sunset Boulevard",
                        "next_stop": 7,
                        "stop_type": "O",
                        "a_time": "09:59"
                    },
                    {
                        "bus_id": 256,
                        "stop_id": 7,
                        "stop_name": "Sesame Street",
                        "next_stop": 0,
                        "stop_type": "F",
                        "a_time": "10:12"
                    },
                    {
                        "bus_id": 512,
                        "stop_id": 4,
                        "stop_name": "Bourbon Street",
                        "next_stop": 6,
                        "stop_type": "S",
                        "a_time": "08:13"
                    },
                    {
                        "bus_id": 512,
                        "stop_id": 6,
                        "stop_name": "Sunset Boulevard",
                        "next_stop": 0,
                        "stop_type": "F",
                        "a_time": "08:16"
                    }
                ]
                    '''


def input_2():
    # On demand stops test:
    # OK
    return '''
                [
                    {
                        "bus_id": 512,
                        "stop_id": 4,
                        "stop_name": "Bourbon Street",
                        "next_stop": 6,
                        "stop_type": "S",
                        "a_time": "08:13"
                    },
                    {
                        "bus_id": 512,
                        "stop_id": 6,
                        "stop_name": "Sunset Boulevard",
                        "next_stop": 0,
                        "stop_type": "F",
                        "a_time": "08:16"
                    }
                ]
            '''


def is_transfer(transfer_lst):
    #  A transfer stop is a stop shared by at least two bus lines
    shared_lst = []
    for i, t in enumerate(transfer_lst):
        for j, t in enumerate(transfer_lst):
            if i != j:
                u = set.intersection(set(transfer_lst[i]), set(transfer_lst[j]))
                shared_lst.append(list(u))
    unique = itertools.chain(*shared_lst)
    shared_unique_lst = list(unique)
    shared_unique_set = set(shared_unique_lst)
    return list(shared_unique_set)

def start():
    # Load json format
    # data = json.loads(input_1())
    # data = json.loads(input_2())
    # data = json.loads(test_1())
    #data = json.loads(test_3())

    data = json.loads(input())

    # get bus-id's
    bus_lines_id = sorted(set([item['bus_id'] for item in data]))

    # validate data
    stop_name_lst = []
    tmp_lst = []
    for bus in bus_lines_id:
        for item in data:
            if item['bus_id'] == bus:
                tmp_lst.append(item['stop_name'])

        stop_name_lst.append(tmp_lst)
        tmp_lst = []

    transfer_stops = is_transfer(stop_name_lst)

    # filter shared
    filter_shared = []
    for bus in bus_lines_id:
        for item in data:
            if item['bus_id'] == bus:
                if item['stop_name'] in transfer_stops:
                    if item['stop_type'] not in ['S', 'F', '']:
                        filter_shared.append(item['stop_name'])

    print("On demand stops test:")
    if filter_shared:
        filter_shared.sort()
        print(f"Wrong stop type: {filter_shared}")
    else:
        print("OK")


if __name__ == '__main__':
    start()
