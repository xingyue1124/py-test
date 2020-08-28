# 二、需求：
# 	1）士兵瑞恩有一把AK47
# 	2）士兵可以开火(士兵开火扣动的是扳机)
# 	3）枪 能够 发射子弹(把子弹发射出去)
# 	4）枪 能够 装填子弹 --增加子弹的数量

class Gun:

    # 创建构造方法，给对象的属性赋值（型号，弹夹中子弹数目）
    def __init__(self,model,bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    # 自定义实例输出方法，替换默认的输出操作
    def __str__(self):
        return "%s，它还有%d颗子弹" %(self.model,self.bullet_count)

    # 创建实例方法，若弹夹中子弹为0输出无子弹，若不为0则数量递减
    def shoot(self):
        if self.bullet_count == 0:
            print("没有子弹了！！！")
            return
        else:
            self.bullet_count -= 1
            print("正在射击...已经射中目标!")
            return

    # 创建实例方法，填充子弹
    def add_bullet(self,count):
            self.bullet_count += count
            print("已经填充了%d颗子弹" % count)
            return

class Soldier:

    # 创建构造方法，给对象的属性赋值（士兵姓名）
    def __init__(self,name):
        self.name = name
        self.gun = None    # 士兵目前没枪，Null是一个类，代表空

    # 自定义实例输出方法，替换默认的输出操作
    def __str__(self):
        return "%s有一把%s" % (self.name,self.gun)

    # 创建实例方法，射击
    def fire(self):
        if self.gun == None:
            print(f'{self.name}没有枪支！！！')
            return
        else:
            self.gun.add_bullet(10)  # 给枪填充10颗子弹
            self.gun.shoot()  # 射击
            return

B = Gun("ak47",30)  # 将枪实例化，ak47且有30颗子弹
A = Soldier("瑞恩")  # 将士兵实例化
A.gun = B  # 将实例化的枪给士兵
# 调用实例方法
A.fire()
print(A)