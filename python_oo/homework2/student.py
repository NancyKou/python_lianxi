#定义私有属性，双下划线加变量名
#调用私有属性或私有方法，则双下划线加类型加 点，则可以找到私有方法或私有比属性
class Student: #定义一个Student类
    def __init__(self,name,score): #初始化参数
        self.name = name  #定义实例变量name
        self.score =score #定义实例变量score

    def grade(self): #定义一个类方法grade
        if self.score >= 90: #如果分数大于等于90分
            print(self.name,',your grade is A！') #打印xx学生的等级为A
        elif self.score >= 60: #如果分数大于等于60分
            print(self.name,',your grade is B.') #打印xx学生的等级为B
        else:
            print(self.name,',your grade is C.') #否则打印xx学生的等级为C

    def work(self):  #定义一个类方法work
        print(f'{self.name}学习很努力！')  #打印XX学生学习很努力。

stu1 = Student('dannie',90) #实例化一个学生1，给init中定义的参数传入name和score参数
stu2 = Student('Alex',59)  #实例化一个学生2，给init中定义的参数传入name和score参数

stu1.grade()   #调用grade方法，打印学生1的等级
stu2.work()    #调用work方法，打印学生2的努力程度
