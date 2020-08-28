from Appium.class_1_execute import *

# 点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

# 先定位整个界面（父级元素）
root_element = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
# 再定位子集元素添加头像按钮
root_element.find_element_by_class_name('android.widget.ImageView').click()