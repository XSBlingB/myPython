print('请输入年龄:')
age = input()
age = int(age)
if age >= 18:
    print('年龄是：%02d'%age)
    print('成年人')
else:
    print('年龄是：%02d'%age)
    print('未成年人')
    #不要少写冒号

if age >= 18:
    print('年龄是：%02d' % age)
    print('成年人')
elif age >= 6:
    print('年龄是：%02d' % age)
    print('青少年')
else:
    print('年龄是：%02d' % age)
    print('儿童')

print('请输入身高（m）：')
h = input() #input返回的都是str
h = float(h)
print('请输入体重（kg）：')
w = input()
w = float(w)
bmi = w/(h*h)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')

