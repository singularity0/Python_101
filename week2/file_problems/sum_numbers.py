import sys


def main():
    filename = sys.argv[1]

    f = open(filename, 'r')

    data = f.read()
    data_split = data.split()

    sum = 0
    # print(data_split)
    for i in data_split:
        sum += int(i)

    print(sum)

    f.close()

if __name__ == '__main__':
    main()

