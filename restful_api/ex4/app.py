from flask import Flask, jsonify
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


if __name__ == "__main__":
    app.run()
