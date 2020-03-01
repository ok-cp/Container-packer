import sys
import os
import time

print('os')
print(os.environ['OS'])

print(time.ctime())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# for i in range(5):
#     print(i)
#     time.sleep(1)

print(sys.path)
print(type(sys.path))

#sys.path.append('C:/py_module')

print(sys.path)

#import module.packer

name = ['cat', 'dog', 'rat']

try:
    z = 'cat'
#    z = 'bkg'
    x = name.index(z)
    print('{} Found it ! {} is '.format(z, x+1))

#except ValueError as e:
except ValueError as e:
    print(e)
    print('Not Fount. ValueError')
else:
    print('Ok! else')
finally:
    print('Ok! Finally')

print('--------------------------------')

try:
    a = 'dog'
    if a == 'cat':
        print('ok cat')
    else:
        raise ValueError
except ValueError:
    print('Occurred Exception!')
else:
    print('Ok! else')



#print(name.index('cat'))
print(name[0])

# List
# a = []
# b = list()
# c = [70, 75, 80, 85]
# d = [1000, 10000, 'Ace', 'Base', 'Captine']
# e = [1000, 10000, ['Ace', 'Base', 'Captine']]
# f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

#Tuple
#여러 개의 자료를 하나의 변수로 관리할 때 사용합니다. 
# 리스트(list)와 거의 같지만, 데이터를 변경할 수 없다는 차이가 있습니다. 
# 따라서 .append() 등 값을 변경하는 메소드는 사용할 수 없고, 조회를 하는 .count(), .index() 메소드만 사용할 수 있습니다.
#jb = (1,2,3,4,5)

#dict = object
#사전은 집합의 일종으로, 키와 값이 하나의 데이터를 만듭니다. 
# 순서가 없고 중복된 데이터를 갖지 않아서, 중복 데이터를 만드는 +, *를 사용할 수 없지만, 
# 키를 이용하여 인덱스기호([])를 사용할 수 있습니다.
#jb = {1:"one", 2:"two", 3:"three"}

#Set
#집합은 여러 개의 자료를 하나의 변수로 관리할 때 사용하는 자료형 중의 하나입니다.
#집합 자료형은 수학의 집합과 같은 성질을 가집니다. 
# 즉, 집합은 중복된 데이터를 가질 수 없고, 순서가 없습니다. 
# 따라서 순서와 관련된 인덱스기호([ ])를 사용할 수 없고, 중복 데이터를 만드는 +, *를 사용할 수 없습니다. 하지만, in, not in, len()은 사용할 수 있습니다.
#jb = {1,2,3,4,5}

if __name__ == "__main__":
    print("test")