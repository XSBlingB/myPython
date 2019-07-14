import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('你好')
    elif len(args) == 2:
        print('你好，%s!' % args[1])
    else:
        print('字段过多！')

if __name__ == '__main__':
    test()

#if __name__ == '__main__' 的意思是：
#当 .py 文件被直接运行时，if __name__ == '__main__' 之下的代码块将被运行；
#当 .py 文件以模块形式被导入时，if __name__ == '__main__' 之下的代码块不会被运行。


#作用域
def _private1(name):
    return '你好,%s!' % name
def _private2(name):
    return '嗨，%s！' % name
def greeting(name):
    if len(name) > 3:
        return _private1(name)
    else:
        return _private2(name)
print(greeting('迪达拉'))
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public