import pymysql

class DBHandler():
    def __init__(self, host='localhost', port=3306,
                 username='root',password='123',
                 db_name='wpf'):
        self.connection = pymysql.connect(host=host,
                                     port=port,
                                     user=username,
                                     password=password,
                                     database=db_name)

    def query_one(self,sql):
        c = self.connection.cursor()
        # self.connection.commit()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return data

if __name__=="__main__":
    sql = "select * from student;"
    print(DBHandler().query_one(sql))