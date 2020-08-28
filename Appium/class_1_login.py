from Appium.class_1_execute import driver,NoSuchElementException

def login():
    # 清空
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    # 输入用户名
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('beryl1124')
    # 输入密码
    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('xy123456')
    # 点击登录按钮
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

# 打开APP后如果有“我”的按钮，直接点击，如果没有执行登录
try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
except NoSuchElementException:
    login()
# 点击“我”的按钮，退出登录，再次登录
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    login()