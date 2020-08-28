# 一、定义名为MyTime的类，其中应有三个实例变量 时hour 分minute 秒second
# 1）为了给对象初始化赋值，编写构造方法，对时分秒附初始值
# 2）为了保证数据的安全性，这三个成员变量应声明为私有、
# 3）对三个属性分别定义封装get和set方法，定义一个main方法，创建一个MyTime类的对象并调用这六个方法。
# class Mytime:
#
#     # 创建构造方法，给对象的属性赋值，并私有化属性
#     def __init__(self,hour,minute,second):
#         self.__hour = hour
#         self.__minute = minute
#         self.__second = second
#
#     # 对三个属性定义封装get和set方法
#     def set_hour(self,hour):
#         self.__hour = hour
#
#     def set_minute(self,minute):
#         self.__minute = minute
#
#     def set_second(self,second):
#         self.__second = second
#
#     def get_hour(self):
#         return self.__hour
#
#     def get_minute(self):
#         return self.__minute
#
#     def get_second(self):
#         return self.__second
#
# if __name__ == '__main__':
#     mt = Mytime(16,23,30)
#     # 访问私有属性：对象._类名__变量名
#     print(mt._Mytime__hour,mt._Mytime__minute,mt._Mytime__second)
#     # 调用实例方法
#     mt.set_hour(16)
#     print(mt.get_hour())
#     mt.set_minute(23)
#     print(mt.get_minute())
#     mt.set_second(30)
#     print(mt.get_second())

# 二、为"无名的粉"写一个类WuMingFen，有三个属性 面码:String theMa  粉的分量(两) int quantity  是否带汤 boolean likeSoup
# 要求：
# 1）写一个构造方法 分别给三个属性赋值。构造出一个WuMingFen类的对象(酸辣面码、2两、带汤)，
# 2）写一个普通方法check()打印对象的三个属性。通过对象调用此方法。
# class WuMingFen:
#
#     # 创建构造方法，给对象的属性赋值
#     def __init__(self,M,Q,S):
#         self.theMa = M
#         self.quantity = Q
#         self.likeSoup = S
#     # 创建实例方法
#     def check(self):
#         print(self.theMa, self.quantity, self.likeSoup)
#
# wmf = WuMingFen('酸辣面码','2两','带汤')
# # 通过对象调用实例方法
# wmf.check()


# 一、摆放家具
# 需求：
# 1）房子有户型，总面积和家具名称列表
# 	新房子没有任何的家具
# 2）家具有名字和占地面积，其中
# 	床：占4平米
# 	衣柜：占2平面
# 	餐桌：占1.5平米
# 3）将以上三件家具添加到房子中
# 4）打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

# class House:
#
#     # 创建构造方法，给对象的属性赋值（户型，总面积，剩余面积，家具名称列表）
#     def __init__(self,house_type,area):
#         self.house_type=house_type
#         self.area=area
#         self.free_area = area
#         self.furniture_list = []
#
#     # 创建实例方法，添加家具（加入一个判断，若家具面积太大，打印无法添加）
#     def add_furniture(self,furniture2):
#         if furniture2.use_area > self.free_area:
#             print('%s家具面积太大，无法添加' % (furniture2.name))
#         self.furniture_list.append(furniture2.name)
#         self.free_area -= furniture2.use_area
#
#     # 自定义实例输出方法，替换默认的输出操作
#     def __str__(self):
#         return f'户型{self.house_type}，总面积:{self.area}，剩余面积:{self.free_area}，家具名称列表:{self.furniture_list}'
#
# class furniture:
#
#     # 创建构造方法，给对象的属性赋值（名字和占地面积）
#     def __init__(self,name,use_area):
#         self.name=name
#         self.use_area=use_area
#
#     # 自定义实例输出方法，替换默认的输出操作
#     def __str__(self):
#         return f'{self.name}家具占地面积为{self.use_area}平方米'
#
# # 实例化家具对象，并输出家具的占地面积
# bed=furniture('bed',4)
# print(bed)
# wardrobe=furniture('wardrobe',2)
# print(wardrobe)
# table=furniture('table',1.5)
# print(table)
#
# # 实例化房子对象，调用实例方法，并输出户型，总面积，剩余面积，家具名称列表
# myhouse=House('四室两厅',128)
# myhouse.add_furniture(bed)
# myhouse.add_furniture(wardrobe)
# myhouse.add_furniture(table)
# print(myhouse)


# 三、编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
# 实现思路及关键代码：
# 	1)定义乐器类Instrument，包括makeSound()方法，此方法中乐器声音："乐器发出美妙的声音！"
# 	2)定义乐器类的子类：二胡Erhu、钢琴Piano和小提琴Violin
# 	二胡Erhu声音："二胡拉响人生"
# 	钢琴Piano声音："钢琴美妙无比"
# 	小提琴Violin声音："小提琴来啦"
# 	3）用main类，多态的方式对不同乐器进行切换

class Instrument:
    def makeSound(self):
        print("乐器发出美妙的声音！")

class Erhu(Instrument):
    def makeSound(self):
        print("二胡拉响人生")

class Piano(Instrument):
    def makeSound(self):
        print("钢琴美妙无比")

class Violin(Instrument):
    def makeSound(self):
        print("小提琴来啦")

def play(obj):
    obj.makeSound()

if __name__ == '__main__':
    e = Erhu()
    p = Piano()
    v = Violin()
    play(e)
    play(p)
    play(v)




