from Appium.class_1_execute import *

# 由于用户名和密码的classname一样，所以需要使用list的形式来定位
driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('beryl1124')
driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys('xy123456')