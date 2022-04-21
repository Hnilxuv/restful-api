from flask import request, jsonify
import datetime
from db import cursor, cnx
from customer_manage import get_customer_by_id
from validator import validate_bill_add


# show bill list
def show_bill():
    cursor.execute("SELECT * FROM BILL")
    data = cursor.fetchall()
    bill_list = []
    for row in data:
        bill = {'id': row[0], 'customer_id': row[1], 'time': row[2]}
        bill_list.append(bill)
    if len(bill_list) > 0:
        return jsonify({'bill': bill_list})
    else:
        return jsonify({'mess', 'no bill is found'})


# add a new bill
def add_bill():
    data = request.get_json()
    validate = validate_bill_add(data)
    if validate != True:
        return jsonify(validate)
    else:
        customer_id = data['customer_id']
        time = datetime.datetime.now()
        if get_customer_by_id(customer_id):
            cursor.execute("insert BILL values (?,?)", customer_id, time)
            cnx.commit()
            return show_bill()
        else:
            return jsonify('Customer is not exist')


# get bill by bill id
def get_bill_by_id(id):
    cursor.execute("Select * From BILL Where bill_id= ?", id)
    data = cursor.fetchall()
    bill_list = []
    for row in data:
        bill = {'id': row[0], 'customer_id': row[1], 'time': row[2]}
        bill_list.append(bill)
    return bill_list


# show bill by bill id
def show_bill_by_id(id):
    data = get_bill_by_id(id)
    if data:
        return jsonify({"bill": data})
    else:
        return jsonify({'mess': 'not found'})


# get bill by customer id
def get_bill_by_cid(cid):
    cursor.execute("Select * From BILL Where customer_id= ?", cid)
    data = cursor.fetchall()
    bill_list = []
    for row in data:
        bill = {'id': row[0], 'customer_id': row[1], 'time': row[2]}
        bill_list.append(bill)
    return bill_list


# show bill by customer id
def show_bill_by_cid(cid):
    data = get_bill_by_cid(cid)
    if data:
        return jsonify({"bill": data})
    else:
        return jsonify({'mess': 'not found'})