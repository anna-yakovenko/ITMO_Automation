class Mammal:
    className = 'Млекопитающее'


class Dog(Mammal): # наследование класса указывается в скобках
    species = 'Canius lupus'


dog = Dog()
print(dog.className) # Млекопитающее (обращение к родительскому классу)