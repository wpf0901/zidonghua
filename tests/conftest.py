# 声明这是一个夹具，这个夹具就是个函数
import pytest

# function级别的夹具
@pytest.fixture()
def function_fixture():
    print("function")
    yield
    print("function fished")

# class级别的夹具
@pytest.fixture(scope='class')
def class_fixture():
    print("class")
    yield
    print("class fished")

# module级别的夹具
@pytest.fixture(scope='module')
def module_fixture():
    print("module")
    yield
    print("module fished")