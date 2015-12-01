import sys


def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()

