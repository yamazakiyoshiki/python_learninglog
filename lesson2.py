r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
      print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s= 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j=', j)
print('i=', i)

x = [1, 2, 3, 4, 5]
#y = x.copy()
y = x[:]
y[0] = 100
print('y=', y)
print('x=', x)

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(y)
print(x)

x = ['a', 'b']
y = x
y[0] = 'p'
print(id(x))
print(id(y))
print(y)
print(x)

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp

print(i, j)

a = 100
b = 200

a, b = b, a
print(a, b)

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)