import os
from common.yaml_read import read_yaml


class config_case:
    def get_file_path(self,path_yaml):
        path = read_yaml(r"E:\\pythonProject0926\tests\setting\db.yaml")
        # 获取当前目录
        curr_path = os.path.abspath(__file__)
        # 获取tests目录的文件地址
        dir_data = os.path.dirname(os.path.dirname(curr_path))
        # 获取case文件
        case_file = os.path.join(dir_data,path[path_yaml])
        return case_file
    def get_url(self):
        return 'http://api.lemonban.com:8766'
# print(config_case().get_file_path("E:\\pythonProject0926\tests\setting\db.yaml"))
# print(config_case().get_url()+"/futureloan/member/register")
# print(config_case().get_url().join("/futureloan/member/register"))
# if __name__ == "__main__":
#     print(config_case().get_file_path("regi_path"))