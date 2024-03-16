num = 1
name = '1'
is_ok = True

new_num = int(name)

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))
print(new_num, type(new_num))
print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',', end='.\n')

#数値
print(2+2)

import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)


#文字列
s = 'test'
print(s)
print('hello')
print("hello")
print('I don\'t know')
print('say"I don\'t know"')
print("say\"I don't know\"")

print('hello. \nHow are you?')
print(r'c:\name\name')

print("##########")
print("""\
line1
line2
line3\
""")
print("##########")

print('Hi.' * 3 + 'Mike.')

print('Py' + 'thon')
print('Py''thon')

s = ('aaaaaaaaaaaaaaa'
      'bbbbbbbbbbbbbb')

print(s)

word = 'Python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:5])
print(word[2:])
word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)

t = 'My name is Mike. Hi Mike.'
print(t)
is_start = t.startswith('My')
print(is_start)

print("###########")

print(t.find('Mike'))
print(t.rfind('Mike'))
print(t.count('Mike'))
print(t.capitalize())
print(t.title())
print(t.upper())
print(t.lower())
print(t.replace('Mike', 'Nancy'))

print('############')
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Yoshiki'
family = 'Yamazaki'
print(f'My name is {name} {family}. Watashi ha {family} {name}')