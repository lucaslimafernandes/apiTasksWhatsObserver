import sqlite3
import datetime

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

connection = sqlite3.connect('crons.db')
connection.row_factory = dict_factory
cur = connection.cursor()

response = cur.execute('select * from crons')

print(response.fetchall())


def show_alarmes():
    sql = """
        select
            c.id, c.nome, c.message, 
            c.c_minute , c.c_hour , c.c_day , c.c_month , c.c_day_week
        from crons c
    """
    response = cur.execute(sql).fetchall()
    return response


print(show_alarmes()[0]['nome'])

print(show_alarmes()[0])


def _check(item):
    cid = item['id']
    cnome = item['nome']
    cmessage = item['message']
    c_minute = item['c_minute']
    c_hour = item['c_hour']
    c_day = item['c_day']
    c_month = item['c_month']
    c_day_week = item['c_day_week']

    print(cnome)

item = show_alarmes()
_check(item[0])


def time_now():
    a = datetime.datetime.now()