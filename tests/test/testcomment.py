from ddt import ddt,data
import unittest
from common.get_data import read_excel_dict
from setting.config import config_case
from common.logger import get_logger
import json
import requests
from jsonpath import jsonpath


login_test_case = read_excel_dict(config_case().get_file_path("login_path"),"Sheet1")
@ddt
class GetData(unittest.TestCase):
    @data(*login_test_case)
    def test_login(self,data):
        get_logger().info(f"获得测试数据{data}")
        url = config_case().get_url()+data["url"]
        method = data["method"]
        header = json.loads(data["header"])
        re_data = json.loads(data["data"])
        expected = json.loads(data["expected"])
        response = requests.request(url=url,method=method,headers=header,json=re_data)
        response_json = response.json()
        token = jsonpath(response_json,"$..token")
        if token is not False:
            token1 = token[0]
            get_logger().info(f"获得token{token1}")
        for k,v in expected.items():
            get_logger().info(f"获得预期结果{v}")
            get_logger().info(f"获得实际结果{response_json[k]}")
            self.assertEqual(v,response_json[k])
        return token1
