'''一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
final_hp = hp-enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜'''

class game:
    def __init__(self):
        self.hp = 1000
        self.power =range(201)
        for self.power in range(201):

    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if final_hp >enemy_final_hp:
            print('I win')
        else:
            print('enemy win')
a = game()
a.fight(500,range(201))