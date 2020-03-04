class Car():
    '''
    Car Class    
    Author : bskim
    Date : 2019.11.09
    Description : Class, Static, Instance, Mehtod
    '''

    # Class variable
    price_per_raise = 1.0

    # Instance variable : _var
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)

    # Instance Method
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company {}, price : {}'.format(self._company, self._details)

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def rasie_price(cls, per):
        if per <=1:
            print('1 gt')
            return
        # Class variable
        cls.price_per_raise = per
        print('Raised Price!')

    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok! car is {}'.format(inst._company)
        return 'Sorry~'

# car Instance
car1 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car2 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})


print(car1)
print(car2)
print()


car1.detail_info()
car2.detail_info()
print()


print(car1.get_price())
print(car2.get_price())
print()


# Car.price_per_raise = 1.4
Car.rasie_price(1.6)

print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Instance req
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# Class req
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
