import sys
import json
from datetime import datetime


def welcome_screen():
    message = ["Hello and Welcome!",
                        "Choose an option.",
                        "1. meal - to write what are you eating now.",
                        "2. list <dd.mm.yyyy> - lists all the meals that you ate that day,"]
    return "\n".join(message)


def read_file():
    f = open("food_list.json", "r+")
    data = json.load(f)
    return data


def start():
    print(welcome_screen())
    while True:
        commands = input("Enter commands:>")
        commands_split = commands.split()
        today = datetime.now()
        today_details = str(today.day) + '.' + str(today.month) + "." + str(today.year)
        f = open('food_list.json', 'r')
        data = json.load(f)
        if commands_split[0] == "meal":

            if data[today_details]:
                data[today_details].append(commands_split[1])
                f_write = open("food_list.json", 'w')
                json.dump(data, f_write)
                f_close = f_write.close()
            else:
                upd = {today_details: [commands_split[1]]}
                data.update(upd)
                f_write = open("food_list.json", 'w')
                json.dump(data, f_write)
                f_close = f_write.close()

        elif commands_split[0] == "list":
            print ("\n".join(data[commands_split[1]]))
            break
        else:
            print("wrong command")
            break
        f_close = f.close()

start()

