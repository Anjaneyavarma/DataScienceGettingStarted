double = lambda x: x%2
print(double(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0), my_list))

print(new_list)

l = list(map(lambda x: (x**2), my_list))
print(l)

two = (lambda x:x+1)(2)
print(two)

full_name= lambda first, last: f'full name; {first} {last}'
print(full_name('tom','cruise'))


function = (lambda x, func: x + func(x))(2, lambda y: y+2)
print(function)
