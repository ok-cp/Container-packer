import sys

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

#print(name.index('cat'))
print(name[0])





if __name__ == "__main__":
    print("test")