print(abs(-567))
a = abs #函数名是指向一个函数对象的引用
print(a(-567))

print(hex(1234))#表示成16进制

def my_abs(x):
    if  not isinstance(x,(int,float)):
        raise TypeError('bad operand type') #数据类型检查
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-890))
#执行到return，函数体就退出 return None可简写成 return

def nop():
    pass
#用pass定义一个空函数，起到占位的作用

age = 0
if age >= 18:
    pass
#pass占位，避免语法错误

#print(my_abs('A'))
#print(abs('A'))

import math
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi /6)
print(x,y)
r = move(100,100,60,math.pi /6)
print(r)
#return返回多个值本质上是返回一个tuple



