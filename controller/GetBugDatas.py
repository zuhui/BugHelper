#!/usr/bin/python3

import psycopg2


def GetDatasFromPostgreSQL():
    #打开数据库连接
    db = psycopg2.connect(database="数据库名",user="帐号",password="密码",host="192.168.18.105",port="35432")

    #使用Cursor（）方法创建一个游标对象cursor
    cursor = db.cursor()

    #使用execute（）方法执行SQL查询

    #cursor.execute("SELECT issues.ID,subject,assigned_to_id,	users.\"id\" as user_id,	concat(users.lastname,users.firstname),	ea.address FROM	issues LEFT JOIN users ON users.\"id\" = issues.assigned_to_id LEFT JOIN email_addresses ea on ea.user_id = users.\"id\" WHERE issues.status_id!=8 ORDER BY issues.assigned_to_id ")
    cursor.execute("""
        SELECT
            issues. ID,
            subject,
            issues.created_on,
            iss."name",
            concat (
                users.lastname,
                users.firstname
            )
        FROM
            issues
        LEFT JOIN users ON users."id" = issues.assigned_to_id
        LEFT JOIN email_addresses ea ON ea.user_id = users."id"
        LEFT JOIN issue_statuses iss ON iss."id" = issues.status_id
        WHERE
            issues.status_id != 8
        ORDER BY
            issues.assigned_to_id
    """)
    #提交sql
    db.commit()

    #使用fetchone()方法获取单条数据

    datas = cursor.fetchall()
    cursor.close()
    db.close()
    return datas


'''
if __name__ == "__main__":
    GetDatasFromPostgreSQL()
'''

