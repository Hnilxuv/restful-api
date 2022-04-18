from flask import request, jsonify
import random as r
from restful_api.ex3.db import cursor, cnx


def customer_show():
    cursor.execute("SELECT * FROM CUSTOMER")
    data = cursor.fetchall()
    cus_list = []
    for row in data:
        cus = {'id': row[0], 'name': row[1], 'phone': row[3]}
        cus_list.append(cus)
    return jsonify({'Customer': cus_list})


def generate_uuid():
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uuid_format = [3, 4]
    for n in uuid_format:
        for i in range(0, n):
            random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
        if n != 4:
            random_string += '-'
    return random_string


def customer_add():
    customer_id = generate_uuid()
    name = request.json['name']
    phone = request.json['phone']
    if name != "" or phone != "":
        cursor.execute("insert CUSTOMER values (?,?,?)", customer_id, name, phone)
        cnx.commit()
        return customer_show()
    else:
        return 'Can not add customer'


def customer_by_id(id):
    cursor.execute("SELECT * FROM CUSTOMER WHERE customer_id = ?", id)
    data = cursor.fetchall()
    if data:
        cus_info = []
        for row in data:
            cus = {'id': row[0], 'name': row[1], 'phone': row[3]}
            cus_info.append(cus)
        return jsonify({'Customer': cus_info})
    else:
        return 'Not found customer'
