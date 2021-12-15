from common.get_data import read_excel_dict
from setting.config import config_case
import unittest
from ddt import ddt,data
import requests
import json
from common import logger
from common.create_data import create_data
import re


case_data = read_excel_dict(config_case().get_file_path("regi_path"),"Sheet1")
@ddt
class TestCase(unittest.TestCase):

    @data(*case_data)
    def test_01(self,case_value):
        logger.get_logger().info(f"测试数据{case_value}")
        # 获取请求数据
        url = config_case().get_url()
        url1 = url+case_value["url"]
        method = case_value["method"]
        header = json.loads(case_value["header"])
        expected = json.loads(case_value["expected"])

        data_json = case_value["data"]
        if "##number##" in data_json:
            mobile = create_data().get_phone_number()
            data_json = data_json.replace("##number##",mobile)
            logger.get_logger().info(mobile)
        data_json = json.loads(data_json)
        # 发起请求

        response = requests.request(url=url1, method=method,headers=header,json=data_json)
        # 获得请求的json数据,实际结果
        repon_json = response.json()
        logger.get_logger().info(repon_json)
        for key,value in expected.items():
            self.assertEqual(value,repon_json[key])


