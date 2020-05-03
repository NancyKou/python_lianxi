import  random

from python_oo.homework3.TongLao import TongLao


class XuZhu(TongLao):  #定义一个XuZhu类，并继承于TongLao
    def read(self):  #定义一个read方法，调用时打印'罪过罪过，你们不要打了。。。'
        print('罪过罪过，你们不要打了。。。')
        super().read()   #super调用父类的read方法

xuzhu = XuZhu(1000,random.uniform(100, 201))         #实例化虚竹，传入童姥的hp和power
xuzhu.read()   #实例化子类方法，调用XuZhu的 read方法
xuzhu.read()  #xuzhu类直接调用tonglao的read方法