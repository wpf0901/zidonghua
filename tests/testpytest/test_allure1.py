# test_a.py
import pytest
import allure


@pytest.fixture(scope="session")
def login():
    print("前置条件：登录")


@allure.step("步骤1")
def step_1():
    print("操作步骤----1")


@allure.step("步骤2")
def step_2():
    print("操作步骤----2")


@allure.step("步骤3")
def step_3():
    print("操作步骤----3")


@allure.epic("epic对大story的一个描述性标签")
@allure.feature("测试模块")
class TestC:
    @allure.testcase("http://www.tc.com")
    @allure.issue("https://www.bug.com/")
    @allure.title("测试用例的标题")
    @allure.story("用户故事:1")
    @allure.severity("blocker")
    def test_1(self, login):
        '''我是用例1的描述内容，看的见我不'''
        step_1()
        step_2()

    @allure.story("用户故事:2")
    def test_2(self, login):
        print("测试用例2")
        step_1()
        step_3()


@allure.epic("epic对大story的一个描述性标签")
@allure.feature("模块块2")
class TestC2():
    @allure.story("用户故事：33")
    def test_3(self, login):
        print("测试用例test_3")
        step_1()

    @allure.story("用户故事：44")
    def test_4(self, login):
        print("测试用例test_4")
        step_3()