class base_class(object):
    def __init__(self, driver):
        self.driver = driver

    # 封装元素定位，匹配所有元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
