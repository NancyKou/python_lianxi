'''
设定一个回合制2人对打游戏。
每个人物都有hp，power，skill
hp代表血量，power代表攻击力，
每三个回合可以使用一次skill，skill将攻击力翻倍
'''
import yaml #导入yaml

class Game:  #定义Game类
    def __init__(self): #定义init私有方法
        battle = yaml.safe_load(open("homework-yaml.yaml"))  #读取game.yaml文件并传递给battle
        default = battle["default"]   #读取字典中的 default
        self.first = default[0]    #读取default中第一个人
        self.second = default[1]   #读取default中第二个人

        #读取第一个人的血量、攻击力和技能
        self.first_hp = battle[self.first]["hp"]
        self.first_power = battle[self.first]["power"]
        self.first_skill = battle[self.first]["skill"]

        #读取第二个人的血量、攻击力和技能
        self.second_hp = battle[self.second]["hp"]
        self.second_power = battle[self.second]["power"]
        self.second_skill = battle[self.second]["skill"]

    def fight(self): #定义 fight方法
        round = 0 #初始化第一回合
        while True:
            print(self.first,"'s hp is",self.first_hp)  #打印每一轮后第一个人的血量
            print(self.second,"'s hp is", self.second_hp) #打印每一轮后第二个人的血量
            round +=1  #每一回合round+1
            if round % 3 == 0: #每3回合使用一次技能，分别计算第一个人和第二个人此回合后的血量
                self.first_hp = self.first_hp - self.second_power * self.second_skill
                self.second_hp = self.second_hp - self.first_power * self.first_skill
            else: #非3的倍数回合时，分别计算第一个人和第二个人每回合后的血量
                self.first_hp = self.first_hp - self.second_power
                self.second_hp = self.second_hp - self.first_power
            if self.first_hp <=0:  #如果第一个人的血量先小于等于0，则判定为第一个人输，第二个人赢
                print("{} lose!".format(self.first))
                print("{} win!".format(self.second))
                break
            elif self.second_hp <=0: #如果第二个人的血量先小于等于0，则判定为第二个人输，第一个人赢
                print("{} lose!".format(self.second))
                print("{} win!".format(self.first))
                break
game = Game()  #实例化Game
game.fight()   #调用fight方法