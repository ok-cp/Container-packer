from math import sqrt

# tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)


# namedtuple
from collections import namedtuple

# Declaration namedtuple 
Point = namedtuple('Point', 'x y')
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng2)
print(l_leng1 == l_leng2)


# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# Create Object
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(p1, p2, p3, p4, p5)
print(p1[0] + p2[1]) 
print(p1.x + p2.y) 
print(p2.x + p1.x)

# Unpacking
x, y = p3
print(x + y)

# namedtuple method
temp = [52, 38] 

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict(), p4._asdict())


# 실 사용 실습
# 반20명 , 4개의 반-> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in [str(n) 
                            for n in range(1,21)]]


print()
print()

print(len(students2))
print(students2)

print()
print()

# 출력
for s in students:
    print(s)
