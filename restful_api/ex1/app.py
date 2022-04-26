
from flask import Flask, Response, jsonify, make_response
import bank_manage as bm

app = Flask(__name__)


@app.route('/')
def index():
    return bm.show_account()


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


@app.route('/<int:id>')
def show_by_id(id):
    return bm.show_acc_by_id(id)


@app.route("/add")
def add():
    try:
        return bm.add_account()
    except KeyError:
        return 'data request is invalid'


@app.route("/<int:id>/deposit")
def deposit(id):
    try:
        return bm.account_deposit(id)
    except KeyError:
        return 'data request is invalid'


@app.route("/<int:id>/withdraw")
def withdraw(id):
    try:
        return bm.account_withdraw(id)
    except KeyError:
        return 'data request is invalid'


if __name__ == "__main__":
    app.run(debug=True, port=8088, use_reloader=False)
