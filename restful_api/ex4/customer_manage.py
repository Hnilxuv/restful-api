from flask import jsonify, request
from db import cursor, cnx
from checking_manage import get_checking_acc_by_cid
from saving_acc_manage import get_saving_acc_by_cid
from validator import validate_cus_add


# show customer list
def show_customer():
    cursor.execute("Select * from customer")
    data = cursor.fetchall()
    cus_list = []
    for item in data:
        cus = {'id': item[0], 'name': item[1], 'acc_quantity': item[2]}
        cus_list.append(cus)
    if cus_list:
        return jsonify({'customer': cus_list})
    else:
        return jsonify({'mess': 'No customer is found'})


# add new customer
def add_customer():
    data = request.get_json()
    name = data['name']
    acc_quantity = 0
    validate = validate_cus_add(data)
    if validate != True:
        return jsonify({'mess': validate_cus_add(data)})
    else:
        cursor.execute("Insert customer values (?,?)", name, acc_quantity)
        cnx.commit()
        return show_customer()


# get customer info by customer id
def get_customer_by_id(id):
    cursor.execute("Select * from customer where customer_id = ?", id)
    data = cursor.fetchall()
    cus_list = []
    for item in data:
        cus = {'id': item[0], 'name': item[1], 'acc_quantity': item[2]}
        cus_list.append(cus)
    return cus_list


# show customer info by customer id
def show_cus_by_id(id):
    cus = get_customer_by_id(id)
    return jsonify({'customer': cus})


# update acc_quantity after add by customer_id
def incr_acc_quantity(customer_id):
    cursor.execute("select acc_quantity from customer where customer_id = ?", customer_id)
    acc_quantity = cursor.fetchone()
    tmp = acc_quantity[0] + 1
    cursor.execute("update customer set acc_quantity = ? where customer_id = ?", tmp, customer_id)
    cnx.commit()


# check acc_no is existed
def check_acc_no_exist(acc_no):
    cursor.execute("select acc_no from saving_account checking_account where acc_no =?", acc_no)
    data = cursor.fetchall()
    if data:
        return True
    else:
        return False


# check customer is existed by customer_id
def check_customer_id_exist(id):
    cursor.execute("select customer_id from customer where customer_id =?", id)
    data = cursor.fetchall()
    if data:
        return True
    else:
        return False


# show all info customer by id
def show_all_info_cus_by_id(id):
    cus = get_customer_by_id(id)
    if cus:
        sa_list = get_saving_acc_by_cid(id)
        ca_list = get_checking_acc_by_cid(id)
        if sa_list and ca_list:
            return jsonify({'Customer': cus, 'saving acc': sa_list, 'checking acc': ca_list})
        elif sa_list and not ca_list:
            return jsonify({'Customer': cus, 'saving acc': sa_list, 'checking acc': 'None'})
        elif sa_list and not ca_list:
            return jsonify({'Customer': cus, 'saving acc': 'None', 'checking acc': ca_list})
        else:
            return jsonify({'Customer': cus, 'saving acc': 'None', 'checking acc': 'None'})
    else:
        return jsonify({'mes': 'no acc is found'})
