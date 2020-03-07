# Sequence
# Container : 서로다른 자료형[list, tuple, collections.deque], 
# Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview]
# 
# mutable(list, bytearray, array.array, memoryview, deque) 
# immutable(tuple, str, bytes)

chars = '+_)(*&^%$#@!~)'
# char[1] = 'T' # immutable
code_list1 = []

for s in chars:
    # Unicode List - ord(str)
    # Character - chr(ord)
    code_list1.append(ord(s))

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
code_list3 = [ord(s) for s in chars if ord(s) > 40]
# Comprehending Lists + Map, Filter
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))


print()
print(code_list2)
print([chr(s) for s in code_list2])

print()
print(code_list3)
print([chr(s) for s in code_list3])

print()
print(code_list4)
print([chr(s) for s in code_list4])


# Generator 
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X), 실행하기 전까지 생성되지 않음.
tuple_g = (ord(s) for s in chars)

print(type(tuple_g))
print(next(tuple_g))


# Generator example
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
     print(s)


# Shallow Copy & Deep Copy
# 사용하지 않는 변수는 _ 로 명시적 표기

# Deep Copy 
# 새로운 자료공간을 구성한 후 내용 복사
marks1 = [['~'] * 3 for _ in range(5)] 

# Shallow Copy 
# 주소만 복사, 원본과 사본이 같은 주소를 참조함
# 사본을 수정하면 원본의 내용도 바뀜, 원본을 수정하면 사본의 내용도 바뀜
marks2 = [['~'] * 3] * 5 

print(marks1)
print(marks2)
print([id(i) for i in marks1]) # id가 각자 다름.
print([id(i) for i in marks2]) # 모든 id가 동일함.
print()

# Modify
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)
print([id(i) for i in marks1])
print([id(i) for i in marks2])



# Unpacking
# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

# x, y, rest = range(10) #Occurred Error 
x, y, *rest = range(10)
# x, y, *rest = range(2)
print(x, y, rest)

print()

# immutable, mutable

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))
l_id = id(l)
m_id = id(m)

print()

l = l * 2
m = m * 2

print(id(l))
print(id(m))
l_id = id(l)
m_id = id(m)

l *= 2
m *= 2
print(id(l))
print(id(m))
lc_id = id(l)
mc_id = id(m)


print(l_id == lc_id)
print(m_id == mc_id)


# sort vs sorted 
# reverse, key=len, key=str.lower, key=func..

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True))
print('sorted -', sorted(f_list, key=len))
print('sorted -', sorted(f_list, key=lambda x: x[-1]))
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()

print('sorted -', f_list)

print()

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)


##################################
# hashtable  적은 리소스로 많은 데이터를 효율적으로 관리
# Key에 Value를 저장하는 구조
# 키 값의 연산결과에 따라 직접 접근 가능한 구조
# 별도 hashtable 구현 없이 Dict 사용가능함.
# Key 값을 해싱 함수 -> 해쉬 주소 -> Key에 대한 Value 참조

# Dict 구조
# print(__builtins__.__dict__)


# # Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print( hash(t1))  # immutable(tuple)
# print(hash(t2)) #  Occurred Error - mutable(List) 


# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# # 주의 # key가 동일하면 value가 overwrite
new_dict3 = {k : v for k , v in source}

print(new_dict3)


# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# immutable Dict
from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only 변경
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key1'] = 'value2'

d['key2'] = 'value2'

print(d)

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화 dis
from dis import dis

print('------') # 조금 더 빠름
print(dis('{10}'))

print('------')
print(dis('set([10])'))

print('------')

# Comprehending Set
from unicodedata import name
print({name(chr(i), '') for i in range(0,256)})