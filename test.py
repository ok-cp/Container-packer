a = [1,2]
b = [2,3]
c = (1,2)
d = (2,3)

print('+ list')
print(a, id(a))
print(b, id(b))
print(a + b, id(a+b))

print('+ tuple')
print(c, id(c))
print(d, id(d))
print(c + d, id(c+d))


print('+= list, tuple')
a +=b
c +=d
print(a, id(a))
print(c, id(c))