from Appium.class_1_execute import *

# app原生元素定位
# id定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('beryl1124')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('xy123456')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()

# name定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("请输入用户名")').send_keys('beryl1124')

# class定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('beryl1124')