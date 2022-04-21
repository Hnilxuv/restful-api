from flask import request, jsonify
from db import cursor, cnxn
from validator import validate_add, validate_amount


# show account list
def show_account():
    cursor.execute("SELECT * FROM account_bank")
    data = cursor.fetchall()
    acc_list = []
    for row in data:
        acc = {'id': row[0], 'name': row[1], 'acc_no': row[2], 'balance': row[3]}
        acc_list.append(acc)
    if acc_list:
        return jsonify({'account list': acc_list})
    else:
        return jsonify({'mess': 'No acc is found'})


# check acc_no is existed
def check_acc_no_exist(acc_no):
    cursor.execute("select acc_no from account_bank where acc_no =?", acc_no)
    data = cursor.fetchall()
    if data:
        return True
    else:
        return False


# add new account
def add_account():
    data = request.get_json()
    validate = validate_add(data)
    if validate != True:
        return jsonify({'mess': validate})
    else:
        name = data['name']
        acc_no = data['acc_no']
        balance = data['balance']
        if not check_acc_no_exist(acc_no):
            cursor.execute("insert account_bank values (?,?,?)", name, acc_no, balance)
            cnxn.commit()
            return show_account()
        else:
            return jsonify({'mess': 'acc_no is exist'})


# get balance by acc id
def get_balance_by_id(id):
    a = cursor.execute("Select balance from account_bank where id= ?", id)
    balance = a.fetchone()
    return balance[0]


# update balance by act, id
def update_balance(id, act, balance, amount):
    if act == 'd':
        balance += amount
    elif act == 'w':
        balance -= amount
    cursor.execute("update account_bank set balance = ? where id= ?", (balance, id))
    cnxn.commit()


# deposit by id
def account_deposit(id):
    if get_account_by_id(id):
        data = request.get_json()
        validate = validate_amount(data)
        if validate != True:
            return jsonify({'mess': validate})
        else:
            amount = data['amount']
            if amount > 0:
                balance = get_balance_by_id(id)
                update_balance(id, 'd', balance, amount)
                return show_acc_by_id(id)
            else:
                return jsonify({'mess': 'invalid'})
    else:
        return jsonify({'mes': 'No acc is found'})


# withdraw by id
def account_withdraw(id):
    if get_account_by_id(id):
        data = request.get_json()
        validate = validate_amount(data)
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


# get account by acc id
def get_account_by_id(id):
    cursor.execute("Select * from account_bank where id = ?", id)
    data = cursor.fetchall()
    acc_list = []
    for row in data:
        acc = {'id': row[0], 'name': row[1], 'acc_no': row[2], 'balance': row[3]}
        acc_list.append(acc)
    return acc_list


# show account by acc id
def show_acc_by_id(id):
    acc_list = get_account_by_id(id)
    if acc_list:
        return jsonify({'acc_list': acc_list})
    else:
        return jsonify({'mes': 'No acc is found'})
