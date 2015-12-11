import json
import sys
from random import randint


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def car_data(self):
        return self.car


class Driver:
    def __init__(self, name, Car):
        self.name = name
        self.Car = Car


class Race:
    race_id = 0

    def __init__(self, drivers_list, crash_chance):
        self.drivers_list = drivers_list
        self.crash_chance = crash_chance
        self.race_id = Race.race_id + 1
        Race.race_id = self.race_id
        self.race_prints()

    def race_prints(self):
        print("Race # {}".format(self.race_id))
        print("####START####")

    def crash(self):
        crashed_list = []
        drivers = Engine.populate_drivers()
        self.car_speeds = Engine.car_speed_list()
        for crash in range(0, 2):  # 2 crashes every time
            crashed_driver = drivers.pop(randint(0, (len(drivers)-1)))
            crashed_list.append(crashed_driver.name)
            self.car_speeds.remove(crashed_driver.Car.max_speed)
        return crashed_list


    def update_crashed(self):
        f = open("result.json", "r")
        data = json.load(f)
        f.close()
        d = {}
        crashed = self.crash()
        for i in range(0, len(crashed)):
            d[crashed[i]] = 0
            print("Unfortunately, {} has crashed.".format(crashed[i]))
        upd = {self.race_id: d}
        f_write = open("result.json", "w")
        data.update(upd)
        json.dump(data, f_write)
        f_write.close()


    def race_standing(self):

        self.update_crashed()
        f = open("result.json", "r")
        data = json.load(f)
        f.close()
        drivers = Engine.populate_drivers()

        for driver in drivers:
            if driver.Car.max_speed == self.car_speeds[0]:
                data[str(self.race_id)][driver.name] = 8
            if driver.Car.max_speed == self.car_speeds[1]:
                data[str(self.race_id)][driver.name] = 6
            if driver.Car.max_speed == self.car_speeds[2]:
                data[str(self.race_id)][driver.name] = 4
            f_write = open("result.json", 'w')
            json.dump(data, f_write)

    def race_top3(self):
        f = open("result.json", 'r')
        data = json.load(f)

        top_by_points = []
        top_by_drivers = []
        for k, v in data[str(self.race_id)].items():
            top_by_drivers.append(k)
            top_by_points.append(v)
        # print(top_by_drivers)
        for i in range(0, 3):
            index = top_by_points.index(max(top_by_points))
            print(top_by_drivers[index], end = " ")
            print ((max(top_by_points)))
            top_by_drivers.pop(index)
            top_by_points.pop(index)


class Chamionship:
    def __init__(self, name,  count_races):
        self.name = name
        self.count_races = count_races

    def generate_races(self):
        print("Running {} races ...".format(Engine.races))
        for every_race in range(0, int(Engine.races)):
            drivers = Engine.populate_drivers()
            race = Race(drivers, 1)
            race.race_standing()
            race.race_top3()

    def general_ranking(self):
        f = open('result.json', 'r')
        datum = json.load(f)
        # print(datum)
        ranking = {}
        for i in range(1, int(Engine.races)+1):
            for driver in datum[str(i)]:
                if not driver in ranking:
                    ranking[driver] = datum[str(i)][driver]
                else:
                    ranking[driver] += datum[str(i)][driver]
        return ranking

    def top3(self):
        print("Total championship standings:")
        ranking = self.general_ranking()
        # print(ranking)
        top_by_points = []
        top_by_drivers = []
        for k, v in ranking.items():
            top_by_drivers.append(k)
            top_by_points.append(v)
        # print(top_by_drivers)
        for i in range(0, 3):
            index = top_by_points.index(max(top_by_points))
            print(top_by_drivers[index], end = " ")
            print ((max(top_by_points)))
            top_by_drivers.pop(index)
            top_by_points.pop(index)


class Engine:
    command_start = sys.argv[1]
    chamionship_name = sys.argv[2]
    races = sys.argv[3]

    def welcome_msg():
        welcome = ["Hello PyRacer!", "Please, call command with the proper argument:"]
        return "\n".join(welcome)

    def starting_race():
        print("Starting a new championship called {} with {} races.".format(Engine.chamionship_name, Engine.races))

    def read_json():
        f = open('cars.json', 'r')
        data = json.load(f)
        return data

    def car_speed_list():
        speeds = []
        for every_item in Engine.populate_drivers():
            speeds.append(every_item.Car.max_speed)
        speeds = speeds[::-1]
        return speeds

    def populate_drivers():
        drivers = []
        for driver_car in Engine.read_json()["people"]:
            for k, v in driver_car.items():
                drivers.append(Driver(k, (Car(v[0], v[1], v[2]))))
        return drivers



Engine.starting_race()
championship = Chamionship(Engine.chamionship_name, Engine.races)
championship.generate_races()
championship.general_ranking()
championship.top3()









