from flask import Flask, make_response, jsonify
import customer_manage as cm
import bill_manage as bm
import product_manage as pm
import billdetail_manage as bdm


app = Flask(__name__)


# show product list
@app.route('/Product')
def show_product():
    return pm.show_product()


# add new product
@app.route('/Product/add')
def product_add():
    return pm.add_product()


# show product by id
@app.route('/Product/<int:id>')
def show_product_by_id(id):
    return pm.show_product_by_id(id)


# show customer list
@app.route('/Customer')
def show_customer():
    return cm.show_customer()


# show customer by customer id
@app.route('/Customer/<string:id>')
def show_customer_by_id(id):
    return cm.show_customer_by_id(id)


# add new customer
@app.route('/Customer/add')
def customer_add():
    return cm.customer_add()


# show bill list by customer id
@app.route('/Customer/<string:id>/Bill')
def show_bill_by_customer_id(id):
    return bm.show_bill_by_cid(id)


# show bill list
@app.route('/Bill')
def show_bill():
    return bm.show_bill()


# add new bill
@app.route('/Bill/add')
def add_bill():
    return bm.add_bill()


# show bill by bill id
@app.route('/Bill/<int:id>')
def show_bill_by_bill_id(id):
    return bm.show_bill_by_id(id)


# show detail of bill by id
@app.route('/Bill/<int:id>/detail')
def show_bill_detail_by_id(id):
    return bdm.show_bill_detail_by_id(id)


# add bill detail by bill id
@app.route('/Bill/<int:id>/add')
def add_bill_detail(id):
    return bdm.bill_detail_add(id)


@app.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({'error': 'not found'}), 400)


@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error': 'not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'error': 'something went wrong'}), 500)

@app.errorhandler(405)
def handle_405_error(_error):
    return make_response(jsonify({'error': 'invalid method'}), 405)


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
