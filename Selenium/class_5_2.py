from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('测码学院')
driver.find_element_by_id('su').click()
sleep(2)


# # 获取抗击疫情a标签的文本信息操作
# el = driver.find_element_by_xpath('//*[@id="virus-2020"]')
# # 常规版
# print(el.text)
#
# # document对象版
# # 1.0 死板模式
# js = "return document.getElementById('virus-2020').innerHTML"
# # 执行JS命令行的操作语句，即在selenium中执行上述JS语句
# text2 = driver.execute_script(js)
# print(text2)
#
# # 2.0 滑溜模式： 获取下标为0的arguments集合中的元素，然后执行获取text的操作
# js = "return arguments[0].innerHTML"
# text3 = driver.execute_script(js, el)
# print(text3)



# 页面滚动
# 上下滚动操作
# js = 'document.scrollingElement.scrollTop=500'
# driver.execute_script(js)
# 左右滚动操作:document.scrollingElement.scrollTo(x,y)，x控制左右，y控制上下
# js = 'document.scrollingElement.scrollTo(200,500)'
# driver.execute_script(js)
# 滚动到元素存在的位置
# el = driver.find_element_by_xpath('//*[@id="content_right"]')
# js = 'arguments[0].scrollIntoView()'
# driver.execute_script(js, el)

sleep(5)
driver.quit()
#
# 弹窗处理，切换到弹窗
web_alert = driver.switch_to.alert
# 确认
web_alert.accept()
# 取消
web_alert.dismiss()
# 输入文本，prompt弹窗
web_alert.send_keys('123123')
# 获取prompt弹窗文本内容
# web_alert.text


