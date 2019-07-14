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

