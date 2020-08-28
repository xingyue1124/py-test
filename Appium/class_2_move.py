from Appium.class_1_execute import *
from time import sleep

#获取屏幕尺寸
def size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

l=size()
print(l)

def left():
    l = size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

for i in range(2):
    left()
    sleep(0.5)