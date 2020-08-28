'''
    自动化中的hello world
'''
# 导入Webdriver模块
from selenium import webdriver
# 导入强制等待
from time import sleep

# 创建chrome浏览器对象
driver = webdriver.Chrome()
# 隐式等待：s为单位  实际等待0~10秒的时间，当元素未找到或者没有立即出现的时候，会继续等待并查找元素
# 每一次元素定位时，都会进行隐式等待。
driver.implicitly_wait(10)

# 访问指定的URL
driver.get('http://www.baidu.com')

# 查找需要操作的元素
we_input = driver.find_element_by_id('kw')

# 对元素进行输入操作
we_input.send_keys('测码学院')

# 点击百度一下按钮，执行本次搜索操作
we_button = driver.find_element_by_id('su')
we_button.click()

driver.find_element_by_xpath('//*[@id="1"]').click()

sleep(5)
driver.quit()
