import random #导入random

class TongLao:  #定义一个天山童姥类TongLao
    def __init__(self,hp,power):  #初始化形参，定义2个实例变量hp和power
        self.hp = hp
        self.power = power
        self.hp = self.hp / 2  # 调用fight_zms方法会将自己的武力值提升10倍，血量缩减2倍
        self.power = self.power * 10

    def see_people(self,name):   # 定义一个see_people方法，同时传入一个name参数
        if name == '无崖子':  #如果传入无崖子，打印 “师弟！！！！”
            print('师弟！！！！')
        elif name == '李秋水':  #如果传入李秋水，打印 “贱人!原来是你！来打一架吧！”
            print('贱人!原来是你！来打一架吧！')
        elif name == '丁春秋':  #如果传入丁春秋，打印 “叛徒！我杀了你!”
            print('叛徒！我杀了你!')
        else:  #如果传入其他人，打印“你是谁？赶紧走开！”
            print('你是谁？赶紧走开！')

    def fight_zms(self,liqs_hp,liqs_power): #定义一个fight_zms天山折梅手方法，同时传入2个参数liqs_hp,liqs_power
        while True:
            self.hp = self.hp - liqs_power
            liqs_hp = liqs_hp - self.power
            print('童姥的血量是',self.hp)  #每次打一轮后分别 打印童姥和李秋水的血量
            print('李秋水的血量是',liqs_hp)
            if self.hp  <= 0:  #如果童姥的血量小于等于0，则打印'童姥我居然输了！'并break
                print('童姥我居然输了！')
                break
            elif liqs_hp <= 0:  #如果李秋水的血量小于等于0，则打印'哈哈，李秋水输了！''并break
                print('哈哈，李秋水输了！')
                break
            else:  #如果童姥血量和李秋水血量相等，则抛出异常'
                raise Exception('抛出异常')

    def read(self):  #定义一个read方法，打印'小和尚，快来帮姥姥打架！'
        print('小和尚，快来帮姥姥打架！')

tonglao = TongLao(1000,random.uniform(100, 201))  #实例化童姥，并传入实参童姥的hp和随机power
tonglao.see_people("李秋水")  #调用see_people方法，并传入参数‘李秋水’
tonglao.fight_zms(1000,random.uniform(100, 201))  #调用天山折梅手方法，并传入李秋水的hp和随机power