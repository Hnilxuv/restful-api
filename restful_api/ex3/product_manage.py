from flask import request, jsonify
from restful_api.ex3.db import cursor, cnx


def product_show():
    cursor.execute("SELECT * FROM PRODUCT")
    data = cursor.fetchall()
    pr_list = []
    for row in data:
        pr = {'id': row[0], 'name': row[1], 'category': row[2], 'brand': row[3], 'price': row[4]}
        pr_list.append(pr)
    return jsonify({'product': pr_list})


def product_add():
    try:
        name = request.json['name']
        category = request.json['category']
        brand = request.json['brand']
        price = request.json['price']
        cursor.execute("insert PRODUCT values (?,?,?,?)", name, category, brand, price)
        cnx.commit()
        return product_show()
    except:
        return 'can not add'
