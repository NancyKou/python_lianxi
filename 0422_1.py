'''def temp():
 #   temp = 22
 #   print("当前室温为：%d度" %temp)
 #   return temp

#def f_temp(x):
 #   f_temp = x + 3
    print("当前华氏室温为：%d度" %f_temp)
x = temp()
f_temp(x)

a = 100
def test():
    print('a=%d'%a)

def test1():
    b = 200
    print('b=%d'%b)
test()
test1()
temp = 0
def temp():
    global temp
    temp = 33

def f_temp():
    print('huashi wendu is %d'%temp)
temp()
f_temp()

a = 100
def test():
    print('a=%d'%a)
    print('b=%d'%b)
    print('c=%d'%c)
b = 20
c =300
test()
 #函数中的多个返回值
def test():
     a = 1
     b = 2
     c = 3
     d =[a,b,c]
     return d

num =test()
print(num[2],num[1])'''

#总结：
#1. 根据有没有参数，有没有返回值
1. 无参数,无返回值
def fun():
    pass
2.有参数，无返回值
def func(参数):
    pass
3.无参数，有返回值
def func()：
    return XXX
4. 有参数，有返回值
def func（参数）:
    return XXX

