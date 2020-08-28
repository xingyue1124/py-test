from Appium.class_1_execute import *

driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('beryl1124')
# *匹配所有节点，光用class是不行的，有很多重复的，所以用到组合定位
driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('xy123456')

driver.find_element_by_xpath('//android.widget.Button').click()
# driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()