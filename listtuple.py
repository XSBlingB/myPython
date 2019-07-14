classmates = ['小明','小红','小刚']
print(len(classmates))
print(classmates)

print(classmates[0])
print(classmates[1])
print(classmates[2])

print(classmates[-1])#最后一个索引使用-1
print(classmates[-2])
print(classmates[-3])

classmates.append('小华')#末尾加元素
print(classmates[-1])

classmates.insert(0,'小王')#指定索引处插入
print(classmates[0])

classmates.pop()#删除末尾元素
print(classmates[-1])

classmates.pop(0)#删除指定元素
print(classmates[0])

classmates[0] = '小兰'
print('当前classmates list是:\n')
print(classmates)

L1 = ['ABC',123,True]
L2 = ['python','java',['asp','php'],'c']
print(L2[2][1])
L3=[]
print(len(L3))

tclassmates = ('猫','狗','狐狸')#()是tuple，一旦确定将无法修改指向，更安全，实际中能用tuple则使用tuple
print(tclassmates)

L = [
    ['苹果','谷歌','微软'],
    ['java','python','c'],
    ['小明','小华','小刚']
]
print(L[0][0])
print(L[1][1])
print(L[2][0])

