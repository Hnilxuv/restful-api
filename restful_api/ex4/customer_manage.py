from flask import  Flask, jsonify, request
import pyodbc

app = Flask(__name__)

cnxn = pyodbc.connect(Trusted_Connection='yes',
                      Driver='{ODBC Driver 17 for SQL Server}',
                      Server='DESKTOP-09AHFD3',
                      Database='ex4')
cursor = cnxn.cursor()


def customer_show():
    cursor.execute("Select * from customer")
    data = cursor.fetchall()
    cus_list = []
    for item in data:
        cus = {'id': item[0], 'name': item[1], 'acc_quantity': item[2]}
        cus_list.append(cus)
    return cus_list


def customer_add():
    id = request.json['id']
    name = request.json['name']
    acc_quantity = request.json['acc_quantity']
    cursor.execute("Insert customer values (?,?,?)", id, name, acc_quantity)
    cnxn.commit()


def saving_acc_show():
    cursor.execute("Select * from saving_account")
    data = cursor.fetchall()
    sa_li = []
    for item in data:
        sa = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'interest_rate': item[4], 'link_code': item[5]}
        sa_li.append(sa)
    return jsonify({''})


def saving_acc_add():
    id = request.json['id']
    customer_id = request.json['customer_id']
    acc_no = request.json['acc_no']
    balance = request.json['balance']
    ir = request.json['ir']
    link_code = request.json['link_code']
    cursor.execute('insert saving_account values (?,?,?,?,?,?)', id, customer_id, acc_no, balance, ir, link_code)
    cnxn.commit()
    cursor.execute('select acc_quantity from customer where customer_id = ?', customer_id)
    acc_quantity = cursor.fetchone()
    tmp = acc_quantity[0] + 1
    cursor.execute("update customer set acc_quantity = ? where customer_id = ?", tmp, customer_id)
    cnxn.commit()
    return saving_acc_show()


def checking_acc_show():
    cursor.execute("Select * from checking_account")
    data = cursor.fetchall()
    ca_li = []
    for item in data:
        ca = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'link_code': item[4]}
        ca_li.append(ca)
    return ca_li


def checking_acc_add():
    id = request.json['id']
    customer_id = request.json['customer_id']
    acc_no = request.json['acc_no']
    balance = request.json['balance']
    link_code = request.json['link_code']
    cursor.execute('insert saving_account values (?,?,?,?,?)', id, customer_id, acc_no, balance, link_code)
    cnxn.commit()
    cursor.execute('select acc_quantity from customer where customer_id = ?', customer_id)
    acc_quantity = cursor.fetchone()
    tmp = acc_quantity[0] + 1
    cursor.execute("update customer set acc_quantity = ? where customer_id = ?", tmp, customer_id)
    cnxn.commit()
    return checking_acc_show()


def customer_by_id(id):
    cursor.execute("Select * from customer where customer_id = ?", id)
    data = cursor.fetchall()
    cus_list = []
    for item in data:
        cus = {'id': item[0], 'name': item[1], 'acc_quantity': item[2]}
        cus_list.append(cus)
    return cus_list


def saving_acc_by_cid(id):
    cursor.execute("Select * from saving_account where customer_id = ?", id)
    data1 = cursor.fetchall()
    sa_li = []
    for item in data1:
        sa = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'interest_rate': item[4], 'link_code': item[5]}
        sa_li.append(sa)
    return sa_li


def checking_acc_by_cid(id):
    cursor.execute("Select * from checking_account where customer_id = ?", id)
    data2 = cursor.fetchall()
    ca_li = []
    for item in data2:
        ca = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'link_code': item[4]}
        ca_li.append(ca)
    return ca_li


