from flask import request, jsonify
from db import cursor, cnx
from validator import validate_prd_add


# show product list
def show_product():
    cursor.execute("select * from dbo.PRODUCT")
    data = cursor.fetchall()
    pr_list = []
    for row in data:
        pr = {'id': row[0], 'name': row[1], 'category': row[2], 'brand': row[3], 'price': row[4]}
        pr_list.append(pr)
    if pr_list:
        return jsonify({'product': pr_list})
    else:
        return jsonify({'mess': 'no product is found'})


# add new product
def add_product():
    data = request.get_json()
    validate = validate_prd_add(data)
    if validate != True:
        return jsonify(validate)
    else:
        name = data['name']
        category = data['category']
        brand = data['brand']
        price = data['price']
        if get_product_by_name(name):
            return jsonify({'mess': 'product is exist'})
        else:
            cursor.execute("insert PRODUCT values (?,?,?,?)", name, category, brand, price)
            cnx.commit()
            return show_product()


# get product by name
def get_product_by_name(name):
    cursor.execute("select product_name from PRODUCT where product_name =?", name)
    data = cursor.fetchall()
    return data


# get product by product id
def get_product_by_id(id):
    cursor.execute("select * from PRODUCT where product_id =?", id)
    data = cursor.fetchall()
    pr_list = []
    for row in data:
        pr = {'id': row[0], 'name': row[1], 'category': row[2], 'brand': row[3], 'price': row[4]}
        pr_list.append(pr)
    return pr_list


# show product by product id
def show_product_by_id(id):
    pr_list = get_product_by_id(id)
    if pr_list:
        return jsonify({'Product': pr_list})
    else:
        return jsonify({'mess': 'No product is found'})
