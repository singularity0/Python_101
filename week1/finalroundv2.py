def count_words(arr):
    result = {}
    for item in arr:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result


def nan_expand(times):
    if times <= 0:
        return ""
    else:
        return ("Not a " * times + 'NaN')


def iterations_of_nan_expand(expanded):
    if not type(expanded) == str:
        return False
    if not expanded[-3:] == 'NaN':
        return False
    expanded = expanded[:-3]
    split = expanded.split('Not a ')
    if any([True for x in split if not x == '']):
        return False
    return sum([1 for x in split if x == ''])-1


def group(arg):
    if not type(arg) == list:
        return False
    result = []
    result.append(([arg[0]]))
    for item in range(1, len(arg)):
        if arg[item] == arg[item-1]:
            result[len(result)-1].append(arg[item])
        else:
            result.append([arg[item]])
    return result


def max_consecutive(items):
    return max([len(x) for x in group(items)])


def gas_stations(distance, tank_size, stations):
    ref_num = tank_size
    min_stations = []
    if stations[len(stations)-1] + ref_num < distance:
        return 'no solution'
    stations.append(distance+1)

    for i in range(0, len(stations)+1):
        if stations[i] > ref_num:
            min_stations.append(stations[i-1])
            ref_num = stations[i-1] + 90
            if ref_num >= distance:
                min_stations.append(stations[i])
                break
    return min_stations[:len(min_stations)-1]


def sum_of_numbers(st):
    for i in range(0, len(st)):
        if not st[i].isdigit():
            st = st.replace(st[i], '@', 1)
    split = st.split('@')
    return sum([int(x) for x in split if x.isdigit()])


def numbers_to_message(arr):
    split = group(arr)
    print(split)
    d = {'a': [2], 'b': [2, 2], 'c': [2, 2, 2],
        'd': [3], 'e': [3, 3], 'f': [3, 3, 3],
        'g': [4], 'h': [4, 4], 'i': [4, 4, 4],
        'j': [5], 'k': [5, 5], 'l': [5, 5, 5],
        'm': [6], 'n': [6, 6], 'o': [6, 6, 6],
        'p': [7], 'q': [7, 7], 'r': [7, 7, 7], 's': [7, 7, 7, 7],
        't': [8], 'u': [8, 8], 'v': [8, 8, 8],
        'w': [9], 'x': [9, 9], 'y': [9, 9, 9], 'z':[9, 9, 9, 9]
        }
#   check for capital letters
    specials = [-1, 0, 1]
    digits_with_3_letters = [2, 3, 4, 5, 6, 8]
    digits_with_4_letters = [7, 9]
    for i in range(0, len(split)):
#   check for loops when selecting letter
        if split[i] not in specials and len(split[i]) > 3 and split[i][0] in digits_with_3_letters:
            # print (i)
            while len(split[i]) >= 3:
                split[i] = split[i][:-3]
        if split[i] not in specials and len(split[i]) > 3 and split[i][0] in digits_with_4_letters:
            while len(split[i]) >= 4:
                split[i] = split[i][:-4]


    print(split)
    result = ''
    for i in range(0, len(split)):
        if split[i] == [-1] :
            continue
        if split[i] == [0]:
            result += ' '
            continue

        for k, v in d.items():
            if split[i] == v:
                if split[i-1] == [1]:
                    result += k.upper()
                else:
                    result += k
    return result


# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))

def message_to_numbers(messsage):
    d = {'a': [2], 'b': [2, 2], 'c': [2, 2, 2],
    'd': [3], 'e': [3, 3], 'f': [3, 3, 3],
    'g': [4], 'h': [4, 4], 'i': [4, 4, 4],
    'j': [5], 'k': [5, 5], 'l': [5, 5, 5],
    'm': [6], 'n': [6, 6], 'o': [6, 6, 6],
    'p': [7], 'q': [7, 7], 'r': [7, 7, 7], 's': [7, 7, 7, 7],
    't': [8], 'u': [8, 8], 'v': [8, 8, 8],
    'w': [9], 'x': [9, 9], 'y': [9, 9, 9], 'z':[9, 9, 9, 9]
    }
    result = []
    for i in messsage:
        # print(i == ' ')
        if i == ' ':
            result.append(0)
            continue
        if i.istitle():
            result.append(1)
            i = i.lower()
        if len(result) > 0 and result[len(result)-1:][0] == d[i][0]:
            result.append(-1)
        # print(result[len(result)-1:])
        for k, v in d.items():
            if i == k:
                for item in v:
                    result.append(item)

    return result

