list = [2,3,5,8,4,6,9,1]

def arr_nums(list):  #定义一个arr_num函数
    for i in range(len(list)-1):    #排序的次数
        print('这是第{}次排序'.format(i))  #打印这是第几次排序
        for j in range(len(list)-i-1):   #对比的次数
            print('这是第{}次对比'.format(j))  #打印这是第几次对比
            if list[j] < list[j+1]:  #如果j<j+1
                list[j],list[j+1] = list[j+1],list[j] # 将j,j+1的位置互换
    return list  #返回list值

a = arr_nums(list)
print('重新排序后的列表为：',a) #打印重新排序后的列表