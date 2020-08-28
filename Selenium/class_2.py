# 导入Webdriver模块
from selenium import webdriver
# 导入强制等待
from time import sleep

# 创建浏览器对象
driver = webdriver.Chrome()

# 访问指定的URL
# driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
driver.get('http://www.baidu.com')

# 窗口最大化
driver.maximize_window()

# 基于ID定位
# driver.find_element_by_id('id')
# 基于name定位
# driver.find_element_by_name('name')
# 基于link text定位
# driver.find_element_by_link_text('注册').click()

# 基于partial link text定位，获取多元素时的操作
# dr = driver.find_elements_by_partial_link_text('百度')[1].click()
# for d in dr:
#     print(d.text)
# class属性定位
# driver.find_element_by_class_name('am-radius').click()
# tagName定位
# dr = driver.find_elements_by_tag_name('a')
# for d in dr:
#     if d.text == '登录':
#         d.click()
#         break
# cssSelector定位
# body > div.am-g.my-content > div > div.am-u-sm-12.am-u-md-6.am-u-lg-4.container-right > div.user-form-container > form > div:nth-child(1) > input
# driver.find_element_by_css_selector(
#     'body > div.am-g.my-content > div > div.am-u-sm-12.am-u-md-6.am-u-lg-4.container-right > div.user-form-container > form > div:nth-child(1) > input').click()
# xpath元素定位
# /html/body/div[4]/div/div[2]/div[2]/form/div[1]/input
# //*[@id="kw"]
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('测码学院')

sleep(5)
driver.quit()
# driver.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div').click()
