class Cars:  #定义一个Cars类
    def __init__(self,colour,wheel):  #车类有颜色、轮子2个属性，这2个属性都通过参数传入
        self.colour = colour
        self.wheel = wheel
        self.light = 2
        #定义一个type方法，并根据车的颜色来判断，如果是蓝色的车则打印蓝色的车是一辆卡车，
        # 如果是黄色的车则打印黄色的车是一辆校车，否则则打印XX颜色的车不知道是啥车
    def type(self):
         if self.colour == 'blue':
             print(f'{self.colour}颜色的车是一辆卡车')
         elif self.colour == 'yellow':
             print(f'{self.colour}颜色的车是一辆校车')

    def kind(self): #定义一个kind方法，判断有2个轮子，打印这是自行车，判断有3个轮子，打印这是三轮车。
        if self.wheel == 2:
            print(f'{self.wheel}个轮子的车是自行车')
        elif self.wheel == 3:
            print(f'{self.wheel}个轮子的车是三轮车')

car1 = Cars('blue',2)  #实例化car1，并传入colour,wheel的参数
car2 = Cars('yellow',3)  #实例化car2，并传入colour,wheel的参数
car1.type()  #调用Cars类的type方法，并打印
car2.kind()  #调用Cars类的kind方法，并打印
print(f'所有的车都有{car1.light}个车灯')  #调用Cars类的light属性，并打印


