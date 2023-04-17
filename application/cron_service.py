import sqlite3
import datetime
import time
import os
import sys
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
#print(BASE_DIR)
sys.path.append(BASE_DIR)
import settings

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

connection = sqlite3.connect(settings.DB_DIR)
connection.row_factory = dict_factory
cur = connection.cursor()




def show_alarmes():
    sql = """
        select
            c.id, c.nome, c.message, 
            c.c_minute , c.c_hour , c.c_day , c.c_month , c.c_day_week ,
            c.unique_execute
        from crons c
    """
    response = cur.execute(sql).fetchall()
    return response


def show_alarmes_s(date):
    sql = """
        select
            c.id, c.nome, c.message, 
            c.c_minute , c.c_hour , c.c_day , c.c_month , c.c_day_week,
            c.unique_execute
        from crons c
        where 
            (c.c_minute = ? or c.c_minute = 999)
            and (c.c_hour = ? or c.c_hour = 999)
            and (c.c_day = ? or c.c_day = 999)
            and (c.c_month = ? or c.c_month = 999)
    """
    response = cur.execute(sql,(date.minute, date.hour, date.day, date.month, )).fetchall()
    return response


def new_alarm(item):
    sql = """
        INSERT into crons (nome, message, c_minute, c_hour, c_day, c_month, c_day_week, unique_execute)
        values (?, ?, ?, ?, ?, ?, ?, ?);
    """
    try:
        response = cur.execute(sql, (
            item['nome'], 
            item['message'], 
            item['c_minute'], 
            item['c_hour'],
            item['c_day'],
            item['c_month'],
            item['c_day_week'],
            item['unique_execute']
            ))
        connection.commit()
        return response.lastrowid
    except sqlite3.OperationalError as err:
        return f'Error: {err}'


def delete_alarm(item_id):
    sql = """
        delete from crons where id = ? ;
    """
    try:
        cur.execute(sql, (item_id, ))
        connection.commit()
        return f'Alarme id: {item_id} deletado!'
    except sqlite3.OperationalError as err:
        return f'Error: {err}'



def update_alarm(item):
    sql = """
        update crons
        set last_execute = ? 
        where id = ? ; 
    """
    try:
        cur.execute(sql, (item['last_execute'], item['id'], ))
        connection.commit()
        #return f'Alarme id: {item_id} update!'
    except sqlite3.OperationalError as err:
        return f'Error: {err}'



def sender(item):
    
    template = f"""id: {item['id']} unico: {bool(item['unique_execute'])}\nnome: {item['nome']}\ndef horário: {item['c_minute']} {item['c_hour']} {item['c_day']} {item['c_month']} {item['c_day_week']}\ntemplate: minute hour day month day_week\nmensagem: {item['message']}"""

    url = f'http://localhost:8000/me/{template}'
    req = requests.get(url)

    datee = datetime.datetime.now()
    datee = datee.strftime('%d/%m/%Y %H:%M')

    update_alarm({'id': item['id'], 'last_execute': datee})

    if bool(item['unique_execute']):
        delete_alarm(item['id'])

    return req.content 



if __name__ == '__main__':
    while True:

        date = datetime.datetime.now()
        
        print(f'{date.day=} {date.month=} {date.year=} {date.hour=} {date.minute=}')

        b = show_alarmes_s(date)
        print(b)
        for i in b:
            sender(i)
        
        time.sleep(60)
    
