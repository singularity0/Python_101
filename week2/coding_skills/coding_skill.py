import json
import sys


def read_people():
    people = sys.argv[1]
    f = open(people, "r")
    data = json.load(f)
    f.close()

    return data

def print_output(dic):
    for k, v in dic.items():
        print(k, v)

def main():
    d = {}
    people = read_people()
    for person in people["people"]:
        for every_skill in person["skills"]:
            if not every_skill["name"] in d:
                d[every_skill["name"]] = person["first_name"] +" " + person["last_name"]
                level = every_skill["level"]
                for item in people["people"]:
                    for skill in item["skills"]:
                        if skill["name"] == every_skill["name"]:
                            if skill["level"] > level:
                                d[every_skill["name"]] = item["first_name"] +" " + item["last_name"]
    return print_output(d)
print(main())

