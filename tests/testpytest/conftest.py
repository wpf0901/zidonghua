import pytest
import pymysql


@pytest.fixture()
def study_fix(study_fix1):
    print("代码开始执行前")
    con = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123", db="wpf")
    my_cursor = con.cursor()
    my_cursor.execute("select * from student")
    print(my_cursor.fetchone())
    yield
    print("代码开始执行后")


@pytest.fixture()
# @pytest.mark.usefixtures("study_fix")
def study_fix1():
    print("测试用例执行前---")
    yield
    print("测试用例执行后---")
