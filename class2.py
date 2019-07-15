class Animal(object):
    def __init__(self,name):
        self.name = name

    def run(self):
        print('%s is running !' % self.name)

    def eat(self):
        print('Animal is eating !')

class Dog(Animal):
    def eat(self):
        print('Dog is eating !')

class Cat(Animal):
    def eat(self):
        print('Cat is eating !')

dog = Dog('小狗')
print(dog.run())
print(dog.eat())

cat = Cat('小猫')
print(cat.run())
print(cat.eat())