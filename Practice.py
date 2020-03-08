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


def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)


var_func = factorial

print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])


print([var_func(i) for i in range(1,10) if i % 2])



# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))