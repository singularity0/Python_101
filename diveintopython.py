# problem descriptions here:
# https://github.com/HackBulgaria/Programming101-Python/tree/master/week01/Dive-Into-Python

def sum_half(n):
    sum = 0
    for i in range(0, len(n)//2):
        sum += int(n[i])
    return sum

def is_number_balanced(n):
    n = str(n)
    sumLR = sum_half(n)
    n = n[::-1]
    sumRL = sum_half(n)
    print(sumRL)
    return sumLR == sumRL

# print(is_number_balanced(9))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))


def is_increasing(seq):
    for i in range(0, len(seq)-1):
        if seq[i+1] <= seq[i]:
            return False
    return True

# print(is_increasing([1, 2, 3, 4, 5]))
# print(is_increasing([1]))
# print(is_increasing([5, 6, -10]))
# print(is_increasing([1, 1, 1, 1]))


def is_decreasing(seq):
    seq = seq[::-1]
    return is_increasing(seq)

# print(is_decreasing([5,4,3,2,1]))
# print(is_decreasing([1,2,3]))
# print(is_decreasing([100, 50, 20]))
# print(is_decreasing([1,1,1,1]))


def is_transversal(transversal, family):
    for i in range (0, len(family)):
        if not any(t in family[i] for t in transversal):
            return False
        else:
            return True
# print(is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6))))
# print(is_transversal((1, 2), ((1, 5), (2, 3), (4, 7))))
# print(is_transversal((2, 3, 4), ((1, 7), (2, 3, 5), (4, 8))))

def generate_transversals(family):
#     for i in range(0, len(family)):
#         for j in
# print(generate_transversals([[1, 4, 5], [2, 7], [1, 9]]))


def is_palindrome(n):
    n = str(n)
    for i in range(0, len(n)//2):
        if n[i] != n[len(n)-1-i]:
            return False
    return True
# print(is_palindrome(99433499))


def get_largest_palindrome(n):
    n = n -1
    while is_palindrome(n) != True:
        n = n - 1
        is_palindrome(n)
    return n
# print(get_largest_palindrome(99))
# print(get_largest_palindrome(994687))

def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True
# print(is_prime(29))


def prime_numbers(n):
    prime_list = []
    for i in range(2,n+1):
        if is_prime(i) == True:
            prime_list.append(i)
    return (prime_list)
# print(prime_numbers(40))
# print(prime_numbers(3))


def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    for i in a:
        b= b.replace(i,'',1)
        a = a.replace(i,'',1)
    if a == b:
        return True
    else:
        return False
# print(is_anagram("BRADE", "BeaRD"))
# print(is_anagram("TOP_CODER", "COTO_PRODE"))


def birthday_ranges(birthdays, ranges):
    birthdays = sorted(birthdays)
    # print(birthdays)
    result = []
    resultX = []
    sum = 0
    counter = []
    counter_j = 0
    for i in range(0, len(ranges)):
        for j in range (ranges[i][0], ranges[i][1]+1):
            # print(j)
            if j in birthdays:
                sum += birthdays.count(j)
        result.append(sum)
        sum = 0
    return result
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)] ))
# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
