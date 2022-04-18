from flask import Flask, request, render_template, url_for, jsonify
import customer_manage as cm
import bill_manage as bm
import product_manage as pm
import billdetail_manage as bdm


app = Flask(__name__)


@app.route('/Product')
def product_show():
    return pm.product_show()


@app.route('/Product/add')
def product_add():
    return pm.product_add()


@app.route('/Customer')
def customer_show():
    return cm.customer_show()


@app.route('/Customer/add', methods=["POST"])
def customer_add():
    return cm.customer_show()


@app.route('/Bill')
def bill_show():
    return bm.bill_show()


@app.route('/Bill/add')
def bill_add():
    return bm.bill_add()


@app.route('/Bill/<int:id>/add')
def bill_detail_add(id):
    return bdm.bill_detail_add(id)


@app.route('/Bill/<int:id>')
def bill_detail_show(id):
    bill_info = bm.bill_by_id(id)
    bill_detail_list = bdm.bill_detail_by_id(id)
    return jsonify({'bill info': bill_info, 'bill_detail_list': bill_detail_list})


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
