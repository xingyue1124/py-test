from selenium import webdriver
# 元素定位的筛选类
from selenium.webdriver.common.by import By
# 强制等待
from time import sleep

# 生成浏览器
driver = webdriver.Chrome()

# 窗体最大化
driver.maximize_window()

# get方法：将指定的URL，填入浏览器中，并进行访问
driver.get('http://39.98.138.157/shopxo/index.php')

# 元素的定位操作(需要导入By包)
driver.find_element(By.XPATH, "//a[text()='登录']").click()
# driver.find_element(By.ID, "kw")
# driver.find_element(By.NAME, "su")
# 等同于如下写法
# driver.find_element_by_xpath()

# 添加等待时间
sleep(5)

# 输入账号
driver.find_element(By.XPATH, '//input[@name="accounts"]').send_keys('666666')
# 输入密码
driver.find_element(By.XPATH, '//input[@name="pwd"]').send_keys('111111')

# 点击登录按钮
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

sleep(3)
# 搜索手机商品
driver.find_element_by_id('search-input').send_keys('手机')
driver.find_element_by_id('ai-topsearch').click()
sleep(3)
# 进入手机详情页
driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[1]/div/a/img').click()
sleep(2)
# 获取标签页的Title
title = driver.title
# 打印Title
print(title)

# 浏览器句柄
handles = driver.window_handles
print(handles)
# 关闭当前页
# driver.close()
# 切换页面，就是切换句柄：切换handles，尽可能保障最多只有两个页面
driver.switch_to.window(handles[1])
sleep(2)

driver.find_element_by_xpath(
    '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[1]').click()
sleep(2)
# 对该句柄页操作完成后，关闭该页面
driver.close()
# 切换回第一个句柄页，在进行其他操作
driver.switch_to.window(handles[0])
driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]/div/a/img').click()

sleep(3)
driver.quit()