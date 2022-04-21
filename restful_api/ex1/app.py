from flask import Flask
import bank_manage as bm

app = Flask(__name__)


@app.route('/')
def index():
    return bm.show_account()


@app.route('/<int:id>')
def show_by_id(id):
    return bm.show_acc_by_id(id)


@app.route("/add")
def add():
    return bm.add_account()


@app.route("/<int:id>/deposit")
def deposit(id):
    return bm.account_deposit(id)


@app.route("/<int:id>/withdraw")
def withdraw(id):
    return bm.account_withdraw(id)


if __name__ == "__main__":
    app.run(debug=True, port=8088, use_reloader=False)
