from flask import request, jsonify
from restful_api.ex3.db import cursor, cnx


def bill_detail_add(id):
    bill_id = id
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    cursor.execute("insert BILL_DETAIL values (?,?,?)", bill_id, product_id, quantity)
    cnx.commit()
    bill_list = bill_detail_by_id(id)
    return jsonify({'bill_detail': bill_list})



def bill_detail_by_id(id):
    cursor.execute("Select * From BILL_DETAIL Where bill_id= ?", id)
    data = cursor.fetchall()
    bill_detail_info = []
    for row in data:
        bd = {'product_id': row[1], 'amount': row[2]}
        bill_detail_info.append(bd)
    return bill_detail_info
