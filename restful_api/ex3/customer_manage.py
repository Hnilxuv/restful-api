from flask import request, jsonify
import random as r
from db import cursor, cnx
from validator import validate_cus_add


# show customer list
def show_customer():
    cursor.execute("SELECT * FROM CUSTOMER")
    data = cursor.fetchall()
    cus_list = []
    for row in data:
        cus = {'id': row[0], 'name': row[1], 'phone': row[2]}
        cus_list.append(cus)
    if cus_list:
        return jsonify({'Customer': cus_list})
    else:
        return jsonify({'mess': 'No customer is found'})


# generate customer id
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


# add new customer
def customer_add():
    data = request.get_json()
    validate = validate_cus_add(data)
    if validate != True:
        return jsonify(validate)
    else:
        customer_id = generate_uuid()
        name = data['name']
        phone = data['phone']
        cursor.execute("insert CUSTOMER values (?,?,?)", customer_id, name, phone)
        cnx.commit()
        return show_customer()


# get customer bt customer id
def get_customer_by_id(id):
    cursor.execute("SELECT * FROM CUSTOMER WHERE customer_id = ?", id)
    data = cursor.fetchall()
    cus_info = []
    for row in data:
        cus = {'id': row[0], 'name': row[1], 'phone': row[2]}
        cus_info.append(cus)
    return cus_info


# show customer by customer id
def show_customer_by_id(id):
    data = get_customer_by_id(id)
    if data:
        return jsonify({'Customer': data})
    else:
        return jsonify({'mess': 'No customer '})
