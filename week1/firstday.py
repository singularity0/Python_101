def sum_of_digits(n):
    n = abs(n)
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum


# def sum_of_digits(num):
#     return sum([int(x) for x in str(num)])
# print(sum_of_digits(-123))


def to_digits(n):
    li = []
    n = str(n)
    for i in n:
        li.append(int(i))
    return li
# def to_digits(n):
#     return [int(x) for x in str(n)]
# print(to_digits(123))
# print(to_digits(123023))


def to_number(digits):
    result = ''
    for i in digits:
        result += str(i)
    result = int(result)
    return result
# print(to_number([1,2,3,5,6]))


def factoriel(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
# print(factoriel(4))


def fact_digits(n):
    n = abs(n)
    n = str(n)
    sum = 0
    for i in n:
        sum += factoriel(int(i))
    return sum
# print(fact_digits(444))


def fibonacci(n):
    sum = 0
    fib = [1, 1]
    if n == 1:
        return [1]
    elif n == 2:
        return fib
    else:
        for i in range(2, n):
            sum += fib[i-2] + fib[i-1]
            fib.append(sum)
            sum = 0
        return fib
# print(fibonacci(10))

def fib_number(n):
    return to_number(fibonacci(n))
# print(fib_number(3))
# print(fib_number(10))

def palindrome(obj):
    # obj_reversed = str(obj)[::-1]
    # if str(obj) == obj_reversed:
    #     return True
    # else:
    #     return False
    obj = str(obj)
    for i in range(0, len(obj)//2):
        if obj[i] != obj[len(obj)-1-i]:
            return False
        else:
            return True
# print(palindrome(121))
# print(palindrome("kapak"))
# print(palindrome("baba"))

def count_vowels(str):
    vowels = 'aeiouy'
    counter = 0
    for i in str:
        if i in vowels:
            counter += 1
    return counter

# def count_vowels(st):
#     vowels = 'aeiouy'
#     return len([x for x in st if x in vowels])
# print(count_vowels("Python"))
# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))


def count_consonants(str):
    vowels = 'aeiouy'
    counter = 0
    str = str.lower()
    for i in str:
        if i.isalpha() and i not in vowels and i.isdigit() == False:
            counter += 1
    return counter
# print(count_consonants("Theistareykjarbunga"))
# print(count_consonants("grrrrgh!"))
# print(count_consonants("A nice day to code!"))


def char_histogram(string):
    d = {}
    for item in string:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d
# print(char_histogram("AAAAaaa!!!"))
# print(char_histogram("Python!"))


def sum_of_divisors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i

    return sum
# print(sum_of_divisors(8))
# print(sum_of_divisors(7))
# print(sum_of_divisors(1000))
# print(sum_of_divisors(1))


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# print(is_prime(8))
# print(is_prime(11))
# print(is_prime(2))
