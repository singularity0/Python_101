import sys


def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    f = open(filename1, 'r')
    f2 = open(filename2, 'r')

    print(f.read())
    print(f2.read())

    f.close()
    f2.close()

if __name__ == '__main__':
    main()
