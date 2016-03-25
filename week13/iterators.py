# class Tiger:
#     def roar(self):
#         print("Tiger roaring")

# class Lion:
#     def __init__(self, name):
#         self.name = name

#     def roar(self):
#         print("Lion roaring")


# def duck_typing(obj):
#     if hasattr(obj, 'roar')\
#         and callable(getattr(obj, 'roar')):
#         obj.roar()


# duck_typing(Tiger())
# duck_typing(Lion("Tim"))

# class Panda:
#     pass


# def create_panda(attributes):
#     panda = Panda()

#     for key, value in attributes.items():
#         setattr(panda, key, value)

#     return panda

# p = create_panda({'name': 'Ivo', 'age': 23, 'weight': 80})
# print(p.age)


class Lion:
    def __init__(self):
        pass

    def random(self):
        return 42

def create_lion(attrs):
    some_lion = Lion()

    for k, v in attrs.items():
        setattr(some_lion, k, v)

    return some_lion

some_lion = create_lion({'name': 'Ivo', 'age': 23, 'weight': 80})
print(some_lion.__dict__)
print(dir(Lion()))


# code = '''1 + 5'''

# print(eval(code))

# def some(x, y):
#     print('a is {} and b is {}'.format(ar[0], {kws for kws in kw }))

# print(some(55, 33, 44, x=3, y=4))

