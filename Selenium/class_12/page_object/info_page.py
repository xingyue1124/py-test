from Selenium.class_12.base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class InforPage(BasePage):
    '''
        页面实现的核心流程：
        1. 获取元素
        2. 定义元素操作行为
        3. 执行核心流程：搜索订单
    '''
    # 页面url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/order/index.html'
    # 定义页面元素
    orders = (By.XPATH, '//*[@id="collapse-nav-business"]/li[1]/a')
    search = (By.XPATH, '//input[@placeholder="订单号/收件信息"]')
    button = (By.XPATH, '/html/body/div[4]/div[3]/div/form/div/div/span/button')

    # 断言的元素

    # 定义元素的操作行为：通过各个元素的操作行为进行函数的封装
    def click_order(self):
        self.locator(self.orders).click()

    def input_txt(self, txt):
        self.locator(self.search).send_keys(txt)

    def click_button(self):
        self.locator(self.button).click()

    def test_infor(self, txt):
        self.visit()
        self.click_order()
        self.input_txt(txt)
        self.click_button()

    # 断言的方法：返回true和false


if __name__ == '__main__':
    driver = webdriver.Chrome()
    ip = InforPage(driver, InforPage.url)
    ip.test_infor('测试')