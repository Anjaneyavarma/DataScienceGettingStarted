def fun(x):
    if x < 1:
        return
    else:
        print(x)
        print()
        print(fun(x-1))
        print()
        print(x)

print(fun(4))

def function(x):
    if x == 0:
        return;
    else:
        function(x-1)
        print(x)
        function(x-1)

print(function(3))