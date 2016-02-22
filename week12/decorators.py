from datetime import datetime


def accepts(str):
    def check_str(func):
        def wrapper(name):
            # func('as')
            if type(name) == str:
                return print(func(name))
            else:
                print('TypeError: Argument 1 of say_hello is not str!')
        return wrapper
    return check_str


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello(44)



def encrypt(some_num):
    def apply_cypher(func):
        result = func()
        cyphered = ''
        for i in result:
            if not i == ' ':
                cyphered += chr(ord(i)+1)
            else:
                cyphered += ' '
        def in_func():
            return cyphered
        return in_func
    return apply_cypher

def log(some_file):
    def f(func):
        f = open(some_file, "a")
        f.write('function was called at {}\n'.format( datetime.now()))
        return(func)
    return f

some_num = 1

@log('log.txt')
@encrypt(some_num)
def caesar_cypher():
    return 'Python is cool!!'


print(caesar_cypher())


def performance(file_name):
    def f(func):
        current = datetime.now()
        execute = func()
        current2 = datetime.now()
        total =  current2 - current
        f = open(file_name, "a")
        f.write('function was called and took {} seconds to complete\n'.format( total ))
        return(func)
    return f


@performance('log2.txt')
def something_heavy():
    some_result = ''
    for i in range(1, 100000):
        some_result += str(i)
    return "I am done!"

print(something_heavy())
