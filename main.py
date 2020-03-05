import sys

class main():

    spec = 'main'

    def __init__(self,name,age):
        super().__init__()

    
    def info(self):
        return '{} is {}'.format(self.name,self.age)

    #List comprehension
    a = [1,2,3,4]
    result = [str(num * 2) for num in a]
    print(result)

    y =[ x for x in range(2,10) ]
    print(y)
    z =[ u for u in range(1,10) ]
    print(z)

print(sys.path)
