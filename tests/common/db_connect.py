import pymysql
from common.yaml_read import read_yaml


class OperationMysql:
    def __init__(self,file):
        self.file = file
    def con_db(self):
        data = read_yaml(self.file)
        con = pymysql.connect(host=data["host"],port=data["port"],database=data["db_name"],user=data["username"],password=data["password"])
        return con

    def select_one(self,sql):
        cursor = self.con_db().cursor()
        cursor.execute(sql)
        feacher_one = cursor.fetchone()
        cursor.close()
        return feacher_one
    def select_many(self,sql,size):
        cursor = self.con_db().cursor()
        cursor.execute(sql)
        feacher_many = cursor.fetchmany(size)
        cursor.close()
        return feacher_many
    def select_all(self,sql):
        cursor = self.con_db().cursor()
        cursor.execute(sql)
        feacher_all = cursor.fetchall()
        cursor.close()
        return feacher_all
#
# if __name__ == "__main__":
#     file_path = r"E:\\pythonProject0926\tests\setting\db.yaml"
#     sql = "select reg_name, id from member limit 5;"
#     db = OperationMysql(file_path)
#     print(db.select_one(sql))
#     db.con_db().close()
