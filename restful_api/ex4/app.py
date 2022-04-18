from flask import Flask, jsonify, request
import customer_manage as cm

app = Flask(__name__)


@app.route('/customer')
def customer_show():
    cus_list = cm.customer_show()
    return jsonify({'customer': cus_list})


@app.route('/customer/add', methods=['POST'])
def customer_add():
    cm.customer_add()
    cus_list = cm.customer_show()
    return jsonify({'customer': cus_list})


@app.route('/saving_account')
def saving_account_show():
    sa_list = cm.customer_show()
    return jsonify({'saving account': sa_list})


@app.route('/saving_account/add')
def saving_account_add():
    cm.saving_acc_add()
    sa_list = cm.customer_show()
    return jsonify({'saving account': sa_list})


@app.route('/checking_account')
def checking_account_show():
    ca_list = cm.checking_acc_show()
    return jsonify({'checking account': ca_list})


@app.route('/checking_account/add')
def checking_account_add():
    cm.checking_acc_add()
    ca_list = cm.checking_acc_show()
    return jsonify({'checking account': ca_list})


@app.route('/customer/<int:id>')
def customer_detail(id):
    cus = cm.customer_by_id(id)
    sa_list = cm.saving_acc_by_cid(id)
    ca_list = cm.checking_acc_by_cid(id)
    return jsonify({'Customer': cus, 'saving acc': sa_list, 'checking acc': ca_list})



if __name__ == "__main__":
    app.run()



