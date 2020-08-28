class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
    def study(self):
        if True:
            print(f'{self.name}在学习')

student1=Student('小明')
student1.study()  # 调用实例方法
student2=Student('小花')
student3=Student('小李')
student4=Student('小亮')
student5=Student('小红')
print('实例化了%s个学生'% Student.count)


