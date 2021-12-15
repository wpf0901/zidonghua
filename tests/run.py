import pytest
from BeautifulReport import BeautifulReport
import unittest
from datetime import datetime
import os


# ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# # 拼接
# filename = f"reports/report-{ts}.html"
# print(ts)
# runner.report('测试', filename=filename)

# time_report = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
# path_report = "test-report-"+time_report
#
# suit = unittest.defaultTestLoader.discover("test")
# BeautifulReport(suit).report(filename=path_report,report_dir="report",description="测试报告")
# if __name__=="__main__":
#     pytest.main(["-s","-v","--html=E:\\pythonProject0926\\tests\\testpytest\\report","test_allure1.py","--alluredir=E:\\pythonProject0926\\tests\\testpytest\\report"])

if __name__ == '__main__':
    # pytest.main(["-sv", "./testpytest/test_py.py"])
    # pytest.main(["-s", "./testpytest/test_py.py","--alluredir=./testpytest/report"])
    pytest.main(['-s','-v',"testpytest/test_py.py::TestPractice::test_02","--reruns=3","--reruns-delay=1",'--alluredir=./allure-results',"--html=./allure-results/abc.html"])
    os.system("allure generate report/ -o ./allure-results/allure-reports/")