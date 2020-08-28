import allure
import pytest

# 需求点
@allure.feature("登录测试")
# 功能点
@allure.story("登录注册")
class TestLogin:
    # 操作步骤
    @allure.step("步骤一：获取用户名")
    def test_user(self):
        user = "admin"
        assert user == "admin"

    # 定义等级
    @allure.severity("critical")
    # 在测试报告中输出链接
    # BUG链接
    @allure.issue("http://www.jira.com")
    # 用例链接
    @allure.testcase("http://www.testlink.com")

    @allure.step("步骤二：获取密码")
    def test_pwd(self):
        with open(r"C:\Users\xingy\PycharmProjects\untitled\api\pytest\allure/1.JPG", "rb") as f:
            context = f.read()
            allure.attach(context, "图片", attachment_type=allure.attachment_type.JPG)
            allure.attach("附件txt文字", "响应报文", allure.attachment_type.TEXT)
        pwd = "123456"
        assert pwd == "123456"

    @allure.step("步骤三：获取token")
    def test_token(self):
        token = "23657DGYUSGD126731638712GE18271H"
        assert token == "23657DGYUSGD126731638712GE18271H"


if __name__ == '__main__':
    pytest.main(['-s', "test_allure2.py", '--alluredir', './report/login'])
