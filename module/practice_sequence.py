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