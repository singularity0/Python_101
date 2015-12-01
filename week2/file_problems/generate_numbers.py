import sys
from random import randint


def main():
    filename = sys.argv[1]
    items = sys.argv[2]
    # randoms = []
    f = open(filename, 'r+')

    for i in range(0, int(items)):
        rand = randint(0, 5)
        f.write(str(rand))
        f.write(' ')

    print(f.read())

    f.close()

if __name__ == '__main__':
    main()


