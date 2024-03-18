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