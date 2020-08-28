from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://pic.baidu.com/")


driver.find_element_by_xpath('//*[@id="sttb"]').click()
sleep(3)

# 上传文件时，直接通过send_keys传入文件的路径+名称+后缀，即可直接上传，但是该方法仅供input使用
driver.find_element_by_xpath('//*[@id="stfile"]').send_keys(r'C:\Users\xingy\Desktop\1.JPG')
sleep(10)
driver.quit()