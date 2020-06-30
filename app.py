from flask import Flask
from flask import request
from flask import render_template
import mysql.connector
# from model.employee import Employee
import model.database as db
from model.item import Item


app = Flask(__name__)

@app.route("/mysql_select")
def mysql_select():
    order = ""
    if "order" in request.args.keys() :
            order = request.args.get("order")

    goods = db.get_goods(order)
    
    params = {
    "asc_check" : order == "ASC",
    "desc_check" : order == "DESC",
    "goods" : goods
    }
    return render_template("goods.html", **params)
