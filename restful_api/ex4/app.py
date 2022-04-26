from flask import Flask, jsonify, make_response
import customer_manage as cm
import saving_acc_manage as sam
import checking_manage as cam

app = Flask(__name__)


# show customer list
@app.route('/customer')
def customer_show():
    return cm.show_customer()


# add new customer
@app.route('/customer/add')
def customer_add():
    return cm.add_customer()


# show saving account
@app.route('/saving_account')
def saving_account_show():
    return sam.show_saving_acc()


# add new saving account
@app.route('/saving_account/add')
def saving_account_add():
    return sam.add_saving_acc()


# show checking account list
@app.route('/checking_account')
def checking_account_show():
    return cam.show_checking_acc()


# add a new checking account
@app.route('/checking_account/add')
def checking_account_add():
    return cam.add_checking_acc()


# show info customer and all account
@app.route('/customer/<int:id>')
def customer_detail(id):
    return cm.show_all_info_cus_by_id(id)


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
    app.run()
