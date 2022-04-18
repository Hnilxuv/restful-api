from flask import request, jsonify
import uuid
import datetime
from restful_api.ex3.db import cursor, cnx


def bill_show():
    cursor.execute("SELECT * FROM BILL")
    data = cursor.fetchall()
    bill_list = []
    for row in data:
        bill = {'id': row[0], 'customer_id': row[1], 'time': row[2]}
        bill_list.append(bill)
    return jsonify({'bill': bill_list})


def bill_add():
    bill_id = uuid.uuid1().int >> 110
    customer_id = request.form.get('customer_id')
    time = datetime.datetime.now()
    if customer_id != "":
        cursor.execute("insert BILL values (?,?,?)", bill_id, customer_id, time)
        cnx.commit()
        return 'done'
    else:
        return 'Can not add bill'


def bill_by_id(id):
    cursor.execute("Select * From BILL Where bill_id= ?", id)
    data = cursor.fetchall()
    bill_list = []
    for row in data:
        bill = {'id': row[0], 'customer_id': row[1], 'time': row[2]}
        bill_list.append(bill)
    return bill_list


