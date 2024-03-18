def say_something():
    s = 'hi'
    return s

print(type(say_something))
result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)

def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)

def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ',drink)
    print('dessert = ',dessert)

menu(entree='beef', dessert='beer', drink='ice')

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

# say_something('Hi!', 'Mike', 'Nance')

t = ('Mike', 'Nancy')
say_something('Hi!', *t)

def menu(food, *args, **kwargs):
    # print(kwargs)
    # for k, v in kwargs.items():
    #     print(k, v)
    print(food)
    print(args)
    print(kwargs)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'desert': 'ice'
}

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param (int): The first parameter.
        param (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """

print(example_func.__doc__)

def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)

def outer(a, b):

    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_info
def sub_num(a, b):
    return a - b
# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

def sample_func2(word):
    return word.lower()
# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())

change_words(l, lambda word: word.lower())

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("##############")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
print(next(g))
print("@@@@@")
print(next(g))
print("@@@@@")
print(next(g))

def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()

print(next(c))
print("@@@@@@")
print(next(c))
print("@@@@@@")
print(next(c))
print("@@@@@@")
print(next(c))
print("@@@@@@")
print(next(c))


t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    r.append(i)

print(r)

r = [i for i in t if i % 2 ==0]

print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]

print(r)

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']
d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

def g():
    for i in range(10):
        yield i

g = g()
print(type(g))

g = (i for i in range(10) if i % 2 == 0)

for x in g:
    print(x)