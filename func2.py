#from func1 import my_abs
#print(my_abs(-1234))
#import sys
#print(sys.path)

def power(x):
    return x*x
ans1 = power(15)
print(ans1)

def power(x,n=2):
    ans = 1
    while n > 0:
        ans = ans*x
        n = n-1
    return ans
ans2 = power(5,3)
print(ans2)

ans3 = power(5)
print(ans3)

def enroll(name,gender,age=8,city='北京'):
    print('姓名:',name)
    print('性别：',gender)
    print('年龄：',age)
    print('城市：',city)
    return

print(enroll('小华','男'))
print(enroll('小明','男','15','上海'))
print(enroll('小芳','女'))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())

def add_End(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_End())
print(add_End())
#str None 都是不变对象，设计程序时，尽可能使用不变对象

#可变参数
def calc1(numbers):#可以是传入list或者tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc1([1,2,3]))
print(calc1((1,2,3)))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc2(1,2,3))
print(calc2())


nums = (1,2,3)
print(calc2(*nums))#*针对的是list\tuple

#关键字参数
def person(name,age,**kw):
    print('姓名:',name,'年龄:',age,'其他：',kw)
print(person('小明',19))
print(person('小华',15,城市='北京'))

extra = {'城市':'上海',
         '职业':'学生',
         '国家':'中国'}
print(person('小花',17,**extra))#**针对的是dict

#命名关键字参数
