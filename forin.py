names = ['小红','小兰','小光']
for name in names:
    print(name)

for name in names:
    print('你好，' + name + '!')

sum1 = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum1 =  sum1 + x
print(sum1)

sum2 = 0
for x in list(range(101)):#range（）生成整数序列从0开始，list（）可以转换为list
    sum2 = sum2 + x
print(sum2)

sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n
    n = n-2
print(sum3)

sum4 = 0
n = 100
while n > 0:
    if n < 10:
        break
    sum4 = sum4 + n
    n = n-1
print(n)
print(sum4) #break是跳出循环体，不再执行

n = 0
while n < 10:
    n = n+1
    if n % 2 == 0:
        continue #continue是跳出本次循环，帮助剔除符合判断条件的内容
    print(n)

