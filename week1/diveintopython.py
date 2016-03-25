def sum_half(n):
    n = str(n)
    sum = 0
    for i in range(0, len(n) // 2):
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
    for i in range(0, len(seq) - 1):
        if seq[i + 1] <= seq[i]:
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
    times = 0
    for i in range(0, len(family)):
        if not any(t in family[i] for t in transversal):
            return False
    return True
    # for i in range (0, len(transversal)):
    #     if transversal[i] in any(j in family[i] for j in family[i]):
    #         return False
    # return True
    #
# print(is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6))))
# print(is_transversal((1, 2), ((1, 5), (2, 3), (4, 7))))
# print(is_transversal((2, 3, 4), ((1, 7), (2, 3, 5), (4, 8))))
# print(is_transversal((4, 5, 6), ((5, 5, 7, 9), (1, 4, 3), (2, 6))))


def is_palindrome(n):
    n = str(n)
    for i in range(0, len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            return False
    return True
# print(is_palindrome(99433499))


def get_largest_palindrome(n):
    n = n - 1
    while is_palindrome(n) != True:
        n = n - 1
        is_palindrome(n)
    # while n >= 0:
    # if is_palindrome(n):
    #     break
    #     n -= 1
    return n


# print(get_largest_palindrome(3))
# print(get_largest_palindrome(994687))


def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True
# print(is_prime(29))


def prime_numbers(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i) == True:
            prime_list.append(i)
    return (prime_list)
# print(prime_numbers(40))
# print(prime_numbers(3))


def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    for i in a:
        b = b.replace(i, '', 1)
        a = a.replace(i, '', 1)
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
        for j in range(ranges[i][0], ranges[i][1] + 1):
            # print(j)
            if j in birthdays:
                sum += birthdays.count(j)
        result.append(sum)
        sum = 0
    return result
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)] ))
# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


def sum_matrix(m):
    sum = 0
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            sum += m[i][j]
            print(sum)
    return sum
# def sum_matrix(matr):
#     # Using list comprehensions
#     return sum([sum(row) for row in matr])

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))



# We are centered at 4.
# How to move to get to 4's neighbors
# 1      2     3
# 8     >4<    7
# 9      5     6
NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == '__main__':
    main()

