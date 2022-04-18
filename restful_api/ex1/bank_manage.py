from flask import request, jsonify
import pyodbc


cnxn = pyodbc.connect(Trusted_Connection='yes',
                      Driver='{ODBC Driver 17 for SQL Server}',
                      Server='DESKTOP-09AHFD3',
                      Database='Bank')
cursor = cnxn.cursor()


def account_show():
    cursor.execute("SELECT * FROM account_bank")
    data = cursor.fetchall()
    acc_list = []
    for row in data:
        acc = {'id': row[0], 'name': row[1], 'acc_no': row[2], 'balance': row[3]}
        acc_list.append(acc)
    return acc_list


def account_add():
    name = request.json['name']
    acc_no = request.json['acc_no']
    balance = request.json['balance']
    if name is not None or acc_no is not None or balance is not None:
        cursor.execute("insert account_bank values (?,?,?)", name, acc_no, int(balance))
        cnxn.commit()
        acc_list = account_show()
        return jsonify({'acc_list': acc_list})
    else:
        return 'Can not create account'


def account_deposit(id):
    amount = request.json['amount']
    if amount > 0:
        a = cursor.execute("Select balance from account_bank where id= ?", id)
        balance = a.fetchone()
        tmp = balance[0] + amount
        cursor.execute("update account_bank set balance = ? where id= ?", (tmp, id))
        cnxn.commit()
        acc_list = account_by_id(id)
        return jsonify({'acc_list': acc_list})
    else:
        return 'invalid data'


def account_withdraw(id):
    amount = request.json['amount']
    cursor.execute("Select balance from account_bank where id= ?", id)
    b = cursor.fetchone()
    balance = b[0]
    cus = account_by_id(id)
    if amount < (balance + balance / 100):
        if int(amount) == 100000:
            am = int(amount) + 1000
            tmp = balance - am
            cursor.execute("update account_bank set balance = ? where id= ?", (tmp, id))
            cnxn.commit()
        else:
            am = int(amount) + int(amount) / 100
            tmp = balance - am
            cursor.execute("update account_bank set balance = ? where id= ?", (tmp, id))
            cnxn.commit()
        return jsonify({"account_info": cus})
    else:
        return 'Can not withdraw'


def account_by_id(id):
    cursor.execute("Select * from account_bank where id = ?", id)
    data = cursor.fetchall()
    if data:
        acc_list = []
        for row in data:
            acc = {'id': row[0], 'name': row[1], 'acc_no': row[2], 'balance': row[3]}
            acc_list.append(acc)
        return acc_list
    else:
        return 'No found account'
