def count_words(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

# print(count_words(["apple", "banana", "apple", "pie"]))
# print(count_words(["python", "python", "python", "ruby"]))


def nan_expand(times):

    # return times*"Not a " if times > 0
    if times > 0:
        return times * 'Not a ' + 'NaN'
    else:
        return ""

# print(nan_expand(0))
# print(nan_expand(1))
# print(nan_expand(2))
# print(nan_expand(3))


def iterations_of_nan_expand(expanded):
    expand_short = expanded[0:len(expanded) - 3]
    expr = "Not a "
    counter = 0
    while len(expand_short) > 0:
        if expand_short[0:6] == expr:
            counter += 1
            expand_short = expand_short[6:]
        else:
            return False
    return counter

# def iterations_of_nan_expand(expanded):
#     if len(expanded) == 0:
#         return 0
#     if expanded.count("Not a NaN") == 0:
#         return False
#     else:
#         return expanded.count("Not a")
# print(iterations_of_nan_expand(""))
# print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
# print(iterations_of_nan_expand('Not a NaN'))
# print(iterations_of_nan_expand("Show these people!"))


def group(obj):
    result = []
    result.append([obj[0]])
    for i in range(1, len(obj)):
        if obj[i] == obj[i - 1]:
            result[len(result) - 1].append(obj[i])
        else:
            result.append([obj[i]])
    return result

# print(group([1,1,1,1]))
# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    counter = 1
    max_counter = 0
    for i in range(1, len(items) - 1):
        if items[i] == items[i + 1]:
            counter += 1
        else:
            counter = 1
        if max_counter <= counter:
            max_counter = counter
    return max_counter

# def max_consecutive(items):
#     result = group(items)
#     max_counter = 0
#     for i in range(0, len(result)):
#         if len(result[i]) > max_counter:
#             max_counter = len(result[i])
#     return max_counter
# print(max_consecutive([1, 2, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5]))


def sum_of_numbers(st):
    sum = 0
    for i in range(0, len(st)):
        if not st[i].isdigit():
            st = st.replace(st[i], 'x', 1)
    st2 = st.split("x")
    for i in st2:
        if i.isdigit():
            sum += int(i)
    return sum

print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))

def numbers_to_message(pressedSequence):
    d ={}
    d['i'] =  [4,4,4]
    d['v'] = [8,8,8]
    d['o'] = [6,6,6]
    d[" "] = [0]
    d['a']  = [2]
    d['b'] = [2,2]
    d['c'] = [2,2,2]

    message = ""
    print(group(pressedSequence))
    for i in (group(pressedSequence)):
        for k,v in d.items():
            if i == v:
                message += k

    return message

# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 6,6,6]))
# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))

def message_to_numbers(st):
    d ={}
    d['i'] =  [4,4,4]
    d['v'] = [8,8,8]
    d['o'] = [6,6,6]
    d[" "] = [0]
    d['a']  = [2]
    d['b'] = [2,2]
    d['c'] = [2,2,2]
    message = ""
    counter = 0
    for i in st:
        if i in d:
            counter += 1
    return counter
# print(message_to_numbers("Ivo"))
