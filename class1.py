class Student1(object):#类名通常首字母大写，括号内为继承的父类
    pass
stud1 = Student1()#创建类的对象
stud1.name = '小明'
print(stud1.name)

class Student2(object):
    def __init__(self,name,score):#类本身相当于模板，所以可以添加一些通用属性给类
        self.name = name
        self.score = score
        return
    def print_score(self):
        print('%s:%s' % (self.name,self.score))
    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

stud2 = Student2('小芳',98)        #相应的建立类的对象时，务必填入对应的属性，self不需要填,self代表的是此类的对象
print(stud2.name)
print(stud2.score)

#数据封装（类的方法）
stud2.print_score()#调用类的方法
print(stud2.get_grade())#调用类的方法

#访问限制
class Student3(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        self.__score = score


stud3 = Student3('小美',67)
stud3.print_score()

stud3.set_name('小花')
stud3.set_score(94)
print(stud3.get_name())
print(stud3.get_score())

#练习
class Student4():
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return  self.__gender
    def set_name(self,name):
        self.__name = name
    def set_gender(self,gender):
        self.__gender = gender

#test
bart = Student4('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
