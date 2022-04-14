import datetime

from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect
import pyodbc
import random as r
import uuid

app = Flask(__name__)

cnx = pyodbc.connect(Trusted_Connection='yes',
                     Driver='{ODBC Driver 17 for SQL Server}',
                     Server='DESKTOP-09AHFD3',
                     Database='sale_manage')
cursor = cnx.cursor()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Product')
def product_show():
    cursor.execute("SELECT * FROM PRODUCT")
    data = cursor.fetchall()
    pr_list = []
    for row in data:
        pr_list.append(row)
    return render_template("Product.html", pr_list=pr_list)


@app.route('/Product/add', methods=["POST"])
def product_add():
    name = request.form.get('name')
    category = request.form.get('category')
    brand = request.form.get('brand')
    price = request.form.get('price')
    if name != "" or category != "" or brand != "" or price != "":
        cursor.execute("insert PRODUCT values (?,?,?,?)", name, category, brand, int(price))
        cnx.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/Customer')
def customer_show():
    cursor.execute("SELECT * FROM CUSTOMER")
    data = cursor.fetchall()
    cus_list = []
    for row in data:
        cus_list.append(row)
    return render_template("Customer.html", cus_list=cus_list)


def generate_uuid():
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uuid_format = [3, 4]
    for n in uuid_format:
        for i in range(0, n):
            random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
        if n != 4:
            random_string += '-'
    return random_string


@app.route('/Customer/add', methods=["POST"])
def customer_add():
    customer_id = generate_uuid()
    name = request.form.get('name')
    phone = request.form.get('phone')
    if name != "" or phone != "":
        cursor.execute("insert CUSTOMER values (?,?,?)", customer_id, name, phone)
        cnx.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/Bill')
def bill_show():
    cursor.execute("SELECT * FROM BILL")
    data = cursor.fetchall()
    bill_list = []
    for row in data:
        bill_list.append(row)
    return render_template("Bill.html", bill_list=bill_list)


@app.route('/Bill/add', methods=["POST"])
def bill_add():
    bill_id = uuid.uuid1().int >> 110
    customer_id = request.form.get('customer_id')
    time = datetime.datetime.now()
    if customer_id != "":
        cursor.execute("insert BILL values (?,?,?)", bill_id, customer_id, time)
        cnx.commit()
    return redirect(url_for('index'))


@app.route('/Bill/Addbilldetail/<int:id>', methods=['GET', 'POST'])
def bill_detail_add(id):
    bill = cursor.execute("Select * From BILL Where bill_id= ?", id)
    b = bill.fetchone()
    bill_info = [b]
    if request.method == 'POST':
        bill_id = id
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        cursor.execute("insert BILL_DETAIL values (?,?,?)", bill_id, product_id, quantity)
        cnx.commit()
        # bill_detail = cursor.execute("Select * From BILL_DETAIL Where bill_id= ?", id)
        # bd = bill_detail.fetchall()
        # bill_detail_info = []
        # for row in bd:
        #     bill_detail_info.append(row)
        return render_template("Add_bill_detail.html", bill_info=bill_info)
    return render_template("Add_bill_detail.html", bill_info=bill_info)


@app.route('/Bill/<int:id>')
def bill_detail_show(id):
    bill = cursor.execute("Select * From BILL Where bill_id= ?", id)
    b = bill.fetchone()
    bill_info = [b]
    bill_detail = cursor.execute("Select * From BILL_DETAIL Where bill_id= ?", id)
    bd = bill_detail.fetchall()
    bill_detail_info = []
    for row in bd:
        bill_detail_info.append(row)
    return render_template("Bill_detail.html", bill_info=bill_info, bill_detail_info=bill_detail_info)


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
