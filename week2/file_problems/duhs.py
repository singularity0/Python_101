# import os
# import sys

# path  = sys.argv[1]

# print(os.stat(path)[6])

from subprocess import call
import sys, errno, os


def main():
    res = 0
    size = 'MB'
    pwd = sys.argv[1]
    res = get_size(pwd, res) / 1024
    if res >= 1000:
        size = 'GB'
        res = res / 1024
    print('{}  size is: {} {}'.format(pwd, res, size))


def get_size(path, size):
    storage = size
    for s_file in os.listdir(path):
        try:
            if os.path.isdir(s_file):
                f_path = os.path.join(path, s_file)
                get_size(f_path, storage)
            storage += os.path.getsize(os.path.join(path, s_file))
        except FileNotFoundError:
            print("No such file {} - symbolic links not allowed", format(s_file))

    return storage



if __name__ == '__main__':
    main()
