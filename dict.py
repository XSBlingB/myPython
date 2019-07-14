names = {'小红':80,'小刚':90,'小明':70,'小吴':60}
print(names['小吴'])
names['小吴'] = 66
print(names['小吴'])
print('小丽' in names) #通过in判断key是否在dict里
print(names.get('小丽'))
print(names.get('小丽','不存在小丽'))
#print(names['小丽'])
names.pop('小吴') #删除某个k-v
for name in names:
    print(name)
    #key必须唯一

s = set([1,1,1,2,3,4,5,6,7,8,8,8])
print(s)
s.add(8)
print(s)
s.add(9)
print(s)
s.remove(8)
print(s) #set是数学意义上的无序、不重复的key集合

s1 = set([1,2,3,4,5,6])
s2 = set([1,2,3,'java','python','c'])
print(s1 & s2)
print(s1 | s2)
 #set和dict的key都要采用不可变对象，list是可变对象，str是不可变对象
