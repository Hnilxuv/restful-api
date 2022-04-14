from flask import Flask, request, render_template, url_for
import pyodbc

from werkzeug.utils import redirect

app = Flask(__name__)

cnxn = pyodbc.connect(Trusted_Connection='yes',
                      Driver='{ODBC Driver 17 for SQL Server}',
                      Server='DESKTOP-09AHFD3',
                      Database='Bank')
cursor = cnxn.cursor()


@app.route('/')
def index():
    cursor.execute("SELECT * FROM account_bank")
    data = cursor.fetchall()
    acc_list = []
    for row in data:
        acc_list.append(row)
    return render_template("index.html", acc_list=acc_list)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get('name')
    acc_no = request.form.get('acc_no')
    balance = request.form.get('balance')
    if name != "" or acc_no != "" or balance != "":
        cursor.execute("insert account_bank values (?,?,?)", name, acc_no, int(balance))
        cnxn.commit()
        return redirect(url_for("index"))
    return redirect(url_for("index"))


@app.route("/deposit/<int:id>", methods=['GET', 'POST'])
def deposit(id):
    acc = cursor.execute("Select * from account_bank where id = ?", id)
    data1 = acc.fetchone()
    acc_info = [data1]

    if request.method == 'POST':
        amount = request.form.get('amount')
        a = cursor.execute("Select balance from account_bank where id= ?", id)
        balance = a.fetchone()
        tmp = balance[0] + int(amount)
        cursor.execute("update account_bank set balance = ? where id= ?", (tmp, id))
        cnxn.commit()
        acc = cursor.execute("Select * from account_bank where id = ?", id)
        data2 = acc.fetchall()
        acc_info1 = []
        for row in data2:
            acc_info1.append(row)
        return render_template("deposit.html", acc_info=acc_info1)
    return render_template("deposit.html", acc_info=acc_info)


@app.route("/withdraw/<int:id>", methods=['GET', 'POST'])
def withdraw(id):
    acc = cursor.execute("Select * from account_bank where id = ?", id)
    data1 = acc.fetchall()
    acc_info = []
    for row in data1:
        acc_info.append(row)
    if request.method == 'POST':
        amount = request.form.get('amount')
        if int(amount) == 100000:
            am = int(amount) + 1000
            a = cursor.execute("Select balance from account_bank where id= ?", id)
            balance = a.fetchone()
            tmp = balance[0] - am
            cursor.execute("update account_bank set balance = ? where id= ?", (tmp, id))
            cnxn.commit()
            acc = cursor.execute("Select * from account_bank where id = ?", id)
            data2 = acc.fetchall()
            acc_info1 = []
            for row in data2:
                acc_info1.append(row)
            return render_template("deposit.html", acc_info=acc_info1)
        else:
            am = int(amount) + int(amount) / 100
            a = cursor.execute("Select balance from account_bank where id= ?", id)
            balance = a.fetchone()
            tmp = balance[0] - am
            cursor.execute("update account_bank set balance = ? where id= ?", (tmp, id))
            cnxn.commit()
            acc = cursor.execute("Select * from account_bank where id = ?", id)
            data2 = acc.fetchall()
            acc_info1 = []
            for row in data2:
                acc_info1.append(row)
            return render_template("withdraw.html", acc_info=acc_info1)
    return render_template("withdraw.html", acc_info=acc_info)


if __name__ == "__main__":
    app.run(debug=True, port=8088, use_reloader=False)
