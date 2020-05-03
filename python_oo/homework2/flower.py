class Plant: #定义一个Plant类

    def __init__(self,leaves,height): #植物有叶子、高度2个属性，这2个属性都通过参数传入
        self.leaves = leaves
        self.height = height

    def shape(self): #定义一个shape方法，判断如果叶子是4片的，则是田字草，如果叶子是3片的则是三叶草
        if self.leaves == 4:
            print(f'{self.leaves}片叶子的植物是田字草。')
        elif self.leaves == 3:
            print(f'{self.leaves}片叶子的植物是三叶草。')

    def kinds(self): #定义一个kinds方法，如果这个植物的高度大于2，打印这个植物是大树，否则打印这个植物是小草。
        if self.height >= 2:
            print(f'{self.height}米高的植物是大树')
        else:
            print(f'{self.height}米高的植物是小草')

plant1 = Plant(4,0.5) #实例化一个plant1，并传入leaves,height的参数
plant2 = Plant(4,5)  #实例化一个plant2，并传入leaves,height的参数
plant1.shape()  #调用Plant类的shape方法，并打印
plant2.kinds()  #调用Plant类的kinds方法，并打印
