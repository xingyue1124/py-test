from Appium.class_1_execute import *

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('55555')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456')

driver.save_screenshot('login.png')
driver.get_screenshot_as_file('./images/login.png')

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()