# ��������һ���оߣ�����о߾��Ǹ�����
import pytest

# function����ļо�
@pytest.fixture()
def function_fixture():
    print("function")
    yield
    print("function fished")

# class����ļо�
@pytest.fixture(scope='class')
def class_fixture():
    print("class")
    yield
    print("class fished")

# module����ļо�
@pytest.fixture(scope='module')
def module_fixture():
    print("module")
    yield
    print("module fished")