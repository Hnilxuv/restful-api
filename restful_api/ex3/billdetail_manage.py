from flask import request, jsonify
from db import cursor, cnx
from product_manage import get_product_by_id
from validator import validate_bill_detail_add


# get bill detail by bill, product id
def get_bill_detail_by_id_pid(id, pid):
    cursor.execute("select bill_id, product_id from BILL_DETAIL where bill_id = ? and product_id = ?", id, pid)
    data = cursor.fetchall()
    return data


# get quantity of existed bill detail
def get_quantity(id):
    cursor.execute("select quantity from BILL_DETAIL where product_id = ?", id)
    data = cursor.fetchone()
    return data[0]

# add bill detail by bill id
def bill_detail_add(id):
    bill_id = id
    data = request.get_json()
    product_id = int(data['product_id'])
    quantity = data['quantity']
    validate = validate_bill_detail_add(data)
    if validate != True:
        return jsonify(validate)
    else:
        if not get_product_by_id(product_id):
            return jsonify('Product is not exist')
        else:
            if not get_bill_detail_by_id_pid(id, product_id):
                cursor.execute("insert BILL_DETAIL values (?,?,?)", bill_id, product_id, quantity)
                cnx.commit()
                return show_bill_detail_by_id(id)
            else:
                q = get_quantity(product_id)
                quantity += q
                cursor.execute("update BILL_DETAIL set quantity = ? where bill_id = ? and product_id = ?", quantity,
                               bill_id, product_id)
                cnx.commit()
                return show_bill_detail_by_id(id)



def get_bill_detail_by_id(id):
    cursor.execute("Select * From BILL_DETAIL Where bill_id= ?", id)
    data = cursor.fetchall()
    bill_detail_info = []
    for row in data:
        bd = {'product_id': row[1], 'amount': row[2]}
        bill_detail_info.append(bd)
    return bill_detail_info


def show_bill_detail_by_id(id):
    bill_list = get_bill_detail_by_id(id)
    if bill_list:
        return jsonify({'bill_detail': bill_list})
    else:
        return jsonify({'mess': 'no bill detail is found'})
