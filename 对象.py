'''class Turtle:
     #类变量
     legs =4
     mouth =1
     eyes =2
     def bite(self):
         print('乌龟咬人')

     def climb(self):
         print('爬啊爬')

#直接调用类属性
print(Turtle.eyes)
print(Turtle.bite)

Turtle()
a =Turtle()

a.eyes
a.bite()

class Drawing:
    area = 100
    style = 'North'

    def sleep(self):
        print('房子可以用来睡觉')
    def cook(self):
        print('房子可以用来做饭')

    def sleepat_room(self):
        print('在卧室')
        self.sleep()

my_house = Drawing()
my_house.sleep()
my_house.cook()

Bob_house = Drawing()
Bob_house.sleep()'''

class Bicycle:
    #定义了run方法，定义的同时需要传入一个km参数
    def run(self,km):
        print('自行车骑的里程数{}')
    def run(self,km):
        print('自行车骑的里程数{}'.format(km))

#bicycle = Bicycle()
#bicycle.run(100)

class EBicycle(Bicycle,):
    def__init__(self,volume):
    self.valume = volume

    def get_value(self):
        print('当前电量为',self.valume)

    def fil_charge(self,vol):
        

b = EBicycle()
b.run(100)










