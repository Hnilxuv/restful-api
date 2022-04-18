from flask import Flask, jsonify

import bank_manage as bm

app = Flask(__name__)


@app.route('/')
def index():
    acc_list = bm.account_show()
    return jsonify({'acc_list': acc_list})


@app.route("/add")
def add():
    return bm.account_add()


@app.route("/deposit/<int:id>")
def deposit(id):
    return bm.account_deposit(id)


@app.route("/withdraw/<int:id>")
def withdraw(id):
    return bm.account_withdraw(id)


if __name__ == "__main__":
    app.run(debug=True, port=8088, use_reloader=False)
