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

a = list()
print(isinstance(a,list))# 判断对象类型
print(isinstance(dog,Animal))
print(isinstance(dog,Dog))#dog既是Dog，也是Animal的对象

def run_twice(animal):
    animal.run()
    animal.run()#定义一个运行两次run方法的函数

print(run_twice(dog))
print(run_twice(cat))

class Tortoise(Animal):
    def eat(self):
        print('Tortoise is eating !')
tortoise = Tortoise('乌龟')

print(run_twice(tortoise))
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：


