def sum_of_digits(n):
    result = 0
    n = abs(n)
    n = str(n)
    for i in n:
        result += int(i)
    return result


def to_digits(n):
    arr = []
    n = str(n)
    for i in n:
        arr.append(int(i))
    return arr


def to_number(digits):
    result = ''
    digits_to_str = []
    for i in digits:
        digits_to_str.append(str(i))
    result = int("".join(digits_to_str))

    # for i in digits:
    # 	result += str(i)

    return result


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def fact_digits(n):
    sum_digits = 0
    n = str(n)
    for i in n:
        sum_digits += factorial(int(i))
    return sum_digits


def fibonacci(n):
    fib_seq = [1, 1]
    if n == 1:
        return [1]
    elif n < 1:
        return('invalid')
    else:
        for i in range(2, n):
            fib_seq.append(
                (fib_seq[len(fib_seq) - 1]) + (fib_seq[len(fib_seq) - 2]))
        return fib_seq


def fib_number(n):
    return to_number(fibonacci(n))


def palindrome(n):
    n = str(n)
    sliced = len(n) // 2
    return n[:sliced] == n[sliced + 1:][::-1]


def count_vowels(st):
    count = 0
    st = st.lower()
    for ch in st:
        if ch in "aeiouy":
            count += 1
    return count


def count_consonants(st):
    count = 0
    st = st.lower()
    for i in st:
        if i not in "aeiouy" and i.isalpha():
            count += 1
        else:
            continue
    return count


def char_histogram(st):
    d = {}
    for key in st:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d
