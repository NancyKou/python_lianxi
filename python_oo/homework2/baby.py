class Baby:  #定义一个baby类
    def __init__(self,mouth,eyes,statu):  #初始化属性
        self.mouth = mouth  #定义实例变量mouth
        self.eyes = eyes  #定义实例变量eyes
        self.statu = statu  #定义实例变量statu

    def mode(self):  #定义一个mode方法
        if self.statu == '1':  #如果statu为1
            print('宝宝心情好!')  #打印宝宝心情好
        elif self.statu == '0': #如果statu为0
            print('宝宝心情不好!') #打印宝宝心情不好

    def cry(self):  #定义一个cry方法
        print(f'宝宝{self.eyes}{self.mouth},他在哭！')

    def study(self): #定义一个study方法
        print(f'宝宝{self.eyes}在认真学习！')

baby1 = Baby('张大嘴巴','闭着眼睛','1')  #实例化一个baby1，并传入mouth,eyes,statu的参数
baby2 = Baby('张大嘴巴','闭着眼睛','0')  #实例化一个baby2，并传入mouth,eyes,statu的参数
baby3 = Baby('闭着嘴巴','睁大眼睛','0')  #实例化一个baby3，并传入mouth,eyes,statu的参数
baby1.mode()  #调用mode方法，打印baby1的心情
baby2.cry()  #调用cry方法，打印baby2哭
baby3.study()  #调用study方法，打印baby3学习