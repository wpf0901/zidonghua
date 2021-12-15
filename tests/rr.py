import json

from jsonpath import jsonpath
a_json = { "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
# print(type(a_json))
# b = jsonpath(a_json,"$.store.book[*].author")
# print(b)
# print(jsonpath(a_json,"$..price"))
"""

书店所有书的作者
所有的作者
store的所有元素。所有的bookst和bicycle
store里面所有东西的price
第三个书
最后一本书
前面的两本书。
 过滤出所有的包含isbn的书。
过滤出价格低于10的书。
所有元素。

"""
# print(jsonpath(a_json,"$..author"))
# print(jsonpath(a_json,"$.store"))
# print(jsonpath(a_json,"$.store.*"))
# print(jsonpath(a_json,"$.store..price"))
# print(jsonpath(a_json,"$..price"))
# print(jsonpath(a_json,"$.store.book[2]"))
# print(jsonpath(a_json,"$.store.book[(@.length-1)]"))
# print(jsonpath(a_json,"$.store.book[0,2]"))



dict_reponse = \
  {
    'code': 0,
    'msg': 'OK',
    'data':
      {
        'id': 1237001403,
        'leave_amount': 5003.0,
        'mobile_phone': '15100002222',
        'reg_name': '小柠檬',
        'reg_time': '2021-10-23 21:40:13.0',
        'type': 1,
        'token_info': {
          'token_type': 'Bearer',
          'expires_in': '2021-10-28 20:57:21',
          'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEyMzcwMDE0MDMsImV4cCI6MTYzNTQyNTg0MX0.I_yYncxXv-Z39wBs2qaWfM_GzjJ5UjLOMmEr-bj3sfICzDc2xuPE_msdVtIExWN-3uFt0n-kNGqMkt8MKmzOlA'
        }
      },
    'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}

import pymysql
def study_fix():
  print("代码开始执行前")
  con = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123", db="wpf")
  my_cursor = con.cursor()
  my_cursor.execute("select * from student")
  print(my_cursor.fetchone())


print(study_fix())
