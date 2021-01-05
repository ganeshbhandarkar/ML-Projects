print("Hello")
a = "     1 2     "
a = a.strip()
#
def func(a):
    x = a.split(' ')
    return int(x[0])+int(x[1])

    #return x[0]+x[1]
print(func(a))
