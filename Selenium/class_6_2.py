'''
    1. 了解流程运行：
        登录——搜索商品——进入商品详情——添加商品属性——添加购物车——购物车检查
    2. 了解实际编写时注意的内容
'''
# 导包selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

# driver的初始设置：
# 创建chromeOptions对象
options = webdriver.ChromeOptions()
# 窗体最大化
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
# 设置隐式等待：一般设置时间会比较长
driver.implicitly_wait(10)
# 生成显式等待对象
wait = WebDriverWait(driver, 10, 0.5)

# 操作流程：测试代码
driver.get('http://39.98.138.157/shopxo/')

# 登录操作实现
driver.find_element_by_xpath('//a[text()="登录"]').click()
driver.find_element_by_name('accounts').send_keys('666666')
driver.find_element_by_name('pwd').send_keys('111111')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
# 判断登录是否成功
wait.until(lambda el: driver.find_element_by_xpath('//a[text()="退出"]'))

# 搜索商品，进入商品详情页
driver.find_element_by_id('search-input').send_keys('手机')
driver.find_element_by_id('ai-topsearch').click()
# //*[@xxxx]/a[1]
cellphone = wait.until(lambda el: driver.find_element_by_xpath('//p[contains(text(),"iPhone 6 Plus")]'))
name = cellphone.text
print(name)
cellphone.click()
# 切换句柄
handles = driver.window_handles
driver.close()
driver.switch_to.window(handles[1])

# 选择商品属性，保存到购物车
# 属性的选择在显式等待或者隐式等待是不起作用的，通过强制等待选择
# data_value = wait.until(lambda el: driver.find_element_by_xpath('//*[@data-value="32G"]'))
# data_value.click()
driver.find_element_by_xpath('//*[@data-value="套餐一"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@data-value="银色"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@data-value="64G"]').click()
sleep(2)
input = driver.find_element_by_xpath('//*[@type="number"]')
input.clear()
input.send_keys('10')
sleep(2)
driver.find_element_by_xpath('//*[@title="加入购物车"]').click()

text = driver.find_element_by_xpath('//*[text()="加入成功"]').text
print(text)

# 进入购物车，校验商品是否存在
driver.find_element_by_xpath('//*[text()="购物车"]').click()
sleep(2)
name1 = driver.find_element_by_xpath('//*[contains(text(),"iPhone 6 Plus")]').text
print(name1)
assert name == name1

sleep(10)
driver.quit()