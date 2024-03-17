x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('1000000')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

a = 10
b = 20

if a > 0 and b > 0:
    print('a and b is positive')

if a > 0 or b > 0:
    print('a or b is positive')

if a > 0 & b > 0:
    print('a and b is positive')

if a > 0 | b > 0:
    print('a or b is positive')

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# False: 0, 0.0, '', [], (), {}, set()
is_ok = 0

if is_ok:
    print('OK!')
else:
    print('NO!')

is_list = [1, 2, 3, 4]

if len(is_list) > 0:
    print('OK!')
else:
    print('NO!')

is_empty = None
print(is_empty)

if is_empty is None:
    print('None!!')

print(1 == True)
print(1 is True)

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

count = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')

# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        # break
        continue
    print(word)

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

for i in range(2, 10, 3):
    print(i)

for _ in range(10):
    print('hello')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)