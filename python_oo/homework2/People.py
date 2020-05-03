class People:  # 定义一个People类
    def __init__(self, hair, name):  # 人有头发、姓名2个属性，这2个属性都通过参数传入
        self.hair = hair
        self.name = name

    def talk(self):  # 定义一个talk方法，并打印有XX颜色头发的XX在谈话。
        print('{} is talking, having {} hair!'.format(self.name, self.hair))

class Chinese_People(People):  # 定义一个Chinese_People类，并继承父类People
    def __init__(self, hair, name, language):  # 初始化参数language
        self.language = language
        super().__init__('black','nancy')  # 继承父类的init属性,并传参给父类

    def sing(self):  # 定义一个sing方法，并打印XX在唱XX歌曲。
        print('{} is singing {} song!'.format(self.name, self.language))

p = People('black', 'kelly')  #实例化一个p，并传参给父类，调用父类talk方法
p.talk()
c = Chinese_People('black', 'kelly', 'chinese')  # 实例化一个c，并传参给子类的参数
c.sing()  # 调用子类的sing方法
