import sys
import re


class Monom:
    def __init__(self, coef=0, var=0, deg=0):
        self.coef = coef
        self.var = var
        self.deg = deg


def split_by_monoms(polynom):
    result = []
    # polynom = re.split('[+ -]', polynom)
    # operations = '+-'
    polynom = polynom.split('+')
    return (polynom)


def parse(split):
    # print(split)
    parsed = []
    for monom in split:

        if 'x' in monom:
            if monom.index('x') == 0:
                monom = Monom(
                    coef=1, var=('x'), deg=monom[monom.index('x') + 2:])
            elif not ('^') in monom:
                monom = Monom(coef=monom[:monom.index('x')], var=('x'))
            else:
                monom = Monom(coef=monom[:monom.index('x')], var=(
                    'x'), deg=monom[monom.index('x') + 2:])
        else:
            monom = Monom(coef=int(monom))

        parsed.append(monom)
        # print(parsed[0].deg)
    return parsed


def calculate_similar(monoms):
    dict_deg = {}
    result_s = []
    for i in monoms:
        if i.var:
            if i.deg:
                # print(i.deg)
                if not i.deg in dict_deg:
                    dict_deg[i.deg] = [i.coef]
                else:
                    dict_deg[i.deg].append(i.coef)
            else:
                if not 0 in dict_deg:
                    dict_deg[0] = [i.coef]
                else:
                    dict_deg[0].append(i.coef)
        else:
            if not 'number' in dict_deg:
                dict_deg['number'] = [i.coef]
            else:
                dict_deg['number'].append(i.coef)
    for k, v in dict_deg.items():
        if len(v) > 1:
            dict_deg[k] = sum([int(x) for x in v])
        else:
            dict_deg[k] = v[0]
    for k, v in dict_deg.items():
        if k == 'number':
            result_s.append(Monom(coef=v))
        elif k == 0:
            result_s.append(Monom(coef=v, var='x'))
        else:
            result_s.append(Monom(coef=v, var='x', deg=k))
    # print(result_s[0].coef)
    return result_s


def derive(expr):
    result = ''
    if (len(expr) == 1 and expr[0].coef == 1):
        result += '1'
        return result
    for i in expr:
        if i.var:
            if result:
                result += '+'
            if i.deg:
                result += str(int(i.deg) * int(i.coef)) + 'x'
                if int(i.deg) > 2:
                    result += '^{}'.format(int(i.deg) - 1)
            else:
                result += str(i.coef)
        else:
            if result:
                continue
            else:
                result += str(0)
    return result


def printing_start(ex):
    ex = ex.replace('+', ' + ')
    print('The derivative of f(x) = {} is:'.format(ex))


def printing_end(ex):
    ex = ex.replace('+', ' + ')
    print('f\'(x) = {}'.format(ex))


def remove_empty_spaces(expression):
    clean = ''
    for i in expression:
        if i == ' ':
            continue
        else:
            clean += i
    return clean


def main():

    polynom = sys.argv[1:]
    polynom_clean = remove_empty_spaces(polynom)
    printing_start(polynom_clean)
    split = split_by_monoms(polynom_clean)
    parsed_monoms = parse(split)
    result_before_derivation = calculate_similar(parsed_monoms)
    derived = derive(result_before_derivation)
    printing_end(derived)

if __name__ == '__main__':
    main()
