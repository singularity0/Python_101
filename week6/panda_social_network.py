import json
import re


class Panda:

    def __init__(self, name, email, gender):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(email, str):
            raise TypeError
        if gender not in ["male", "female"]:
            raise TypeError
        self.__name = name
        self.__email = email
        self.__gender = gender

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def __str__(self):
        return "I am Panda. My name is {}".format(self.__name)

    def __repr__(self):
        return "Panda: {}, {}, {} ".format(self.__name,
                                           self.__email,
                                           self.__gender)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(self.__str__())

    def valid_email(self):
        match = re.search(r'[^@|\s]+@[^@]+\.[^@|\s]+', self.__email)

        if match:
            return ("valid email: {}".format(match.group()))
        else:
            return ("not valid email")

    def isMale(self):
        return self.gender() == "male"

    def isFemale(self):
        return self.gender() == "female"


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

    def has_panda(self, panda):
        return panda in self.social_network

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("PandaAlreadyThere")

        self.social_network[panda] = []

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("Pandas are already friends")

        self.social_network[panda1].append(panda2)
        self.social_network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return (panda1 in self.social_network[panda2] and
                panda2 in self.social_network[panda1])

    def friends_of(self, panda):
        if panda not in self.social_network:
            raise Exception("Panda not in the social network")
        return self.social_network[panda]

    def panda_connections(self, panda):
        connections = {}

        q = []
        visited = set()

        q.append((0, panda))
        visited.add(panda)

        while len(q) != 0:
            panda_data = q.pop(0)
            current_level = panda_data[0]
            current_node = panda_data[1]

            connections[current_node] = current_level

            for neighbour in self.social_network[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((current_level + 1, neighbour))

        return connections

    def connection_level(self, panda1, panda2):
        panda_table = self.panda_connections(panda1)

        if panda2 not in panda_table:
            return -1

        return panda_table[panda2]

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    def how_many_gender_in_network(self, level, panda1, gender):
        panda_table = self.panda_connections(panda1)
        counter = 0

        for panda in panda_table:
            p_level = panda_table[panda]
            if (p_level != 0 and
                    p_level <= level and
                    panda.gender() == gender):
                counter += 1

        return counter

    def data(self):
        for_save = {}

        for panda in self.social_network:
            friends = [
                repr(p_friend) for p_friend in self.social_network[panda]
            ]
            for_save[repr(panda)] = friends

        return for_save

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.data(), indent=4))
            f.close()

    # @staticmethod
    def load(self, filename):
        with open(filename, "r") as f:
            contents = f.read()
            filedata = json.loads(contents)


def main():
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")

    for panda in [ivo, rado, tony]:
        network.add_panda(panda)

    network.make_friends(ivo, rado)
    network.make_friends(rado, tony)

    network.connection_level(ivo, rado) == 1  # True
    network.connection_level(ivo, tony) == 2  # True

    network.how_many_gender_in_network(1, rado, "female") == 1  # True
    # print(network)
    # network.save("json.txt")
    network.load("json.txt")


if __name__ == '__main__':
    main()
