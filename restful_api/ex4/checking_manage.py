from flask import jsonify, request
from db import cursor, cnx
import customer_manage as cm
from validator import validate_acc_add


def show_checking_acc():
    cursor.execute("Select * from checking_account")
    data = cursor.fetchall()
    ca_li = []
    for item in data:
        ca = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'link_code': item[4]}
        ca_li.append(ca)
    if ca_li:
        return jsonify({'checking account': ca_li})
    else:
        return jsonify({'mess': 'no checking account is found'})


def add_checking_acc():
    data = request.get_json()
    customer_id = data['customer_id']
    acc_no = data['acc_no']
    balance = data['balance']
    link_code = data['link_code']
    validate = validate_acc_add(data)
    if validate != True:
        return jsonify({'mess': validate})
    else:
        if not cm.check_customer_id_exist(customer_id):
            return jsonify({'mess': 'customer is not exist'})
        else:
            if cm.check_acc_no_exist(acc_no):
                return jsonify({'mess': 'acc_no is exist'})
            else:
                cursor.execute('insert saving_account values (?,?,?,?)', customer_id, acc_no, balance, link_code)
                cnx.commit()
                cm.incr_acc_quantity(customer_id)
                return show_checking_acc()


def get_checking_acc_by_cid(id):
    cursor.execute("Select * from checking_account where customer_id = ?", id)
    data2 = cursor.fetchall()
    ca_li = []
    for item in data2:
        ca = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'link_code': item[4]}
        ca_li.append(ca)
    return ca_li


def show_checking_acc_by_cid(id):
    ca = get_checking_acc_by_cid(id)
    if ca:
        return jsonify({'checking acc': ca})
    else:
        return jsonify({'mess': 'no checking account is found'})


# deposit from checking account
def deposit_checking_acc(id):
    if get_checking_acc_by_cid(id):
        amount = request.json['amount']
        if amount > 0:
            a = cursor.execute("Select balance from checking_account where id= ?", id)
            balance = a.fetchone()
            tmp = balance[0] + amount
            cursor.execute("update saving_account set balance = ? where id= ?", (tmp, id))
            cnx.commit()
            show_checking_acc_by_cid(id)
        else:
            return 'invalid data'
    else:
        return jsonify({'no saving account is found'})


def account_withdraw(id):
    if get_checking_acc_by_cid(id):
        data = request.get_json()
        validate = validate_acc_add(data)
        if validate != True:
            return jsonify({'mess': validate})
        else:
            amount = data['amount']
            balance = get_balance_by_id(id)
            if (amount + balance/100) <= balance:
                if amount <= 100000:
                    amount += 1000
                    update_balance(id, 'w', balance, amount)
                    return show_acc_by_id(id)
                else:
                    amount += amount/100
                    update_balance(id, 'w', balance, amount)
                    return show_acc_by_id(id)
            else:
                return 'balance is not enough to withdraw'
    else:
        return jsonify({'mes': 'No acc is found'})
