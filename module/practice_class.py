
class Car():
    def __init__(self, company, detail):
        self._company = company
        self._details = detail

    # instance def
    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)


car1 = Car('BMW', {'color': 'White', 'power': 400, 'price': 8000})

print(car1)
print(car1.__dict__)