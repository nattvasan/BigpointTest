from flask import Flask
from flask import request
import sqlite3
import json

app = Flask(__name__)
@app.route("/cart/fetch/<itemID>", methods=["GET"])
def fetchFromCart(itemID):
    tableName= "cart"
    conn = sqlite3.connect("myDb/cart.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM {tn} where itemId="{id}"'.format(tn=tableName,
                                                                id=itemID))
    all_rows = cur.fetchall()
    conn.commit()
    conn.close()
    jsonObj = json.dumps(all_rows)
    return str(jsonObj)

@app.route("/cart/addToCart/", methods=["POST"])
def addToCart():
    tableName = "cart"
    conn = sqlite3.connect("myDb/cart.db")
    cur = conn.cursor()
    dat = {
        'name': request.json['name']
    }
    cur.execute("INSERT INTO {tn} ({name}) VALUES('{val}')".format(
        tn=tableName,name="itemName",val=str(dat["name"])))
    print
    conn.commit()
    conn.close()
    return "{} :Item Added to cart".format(str(dat["name"]))

if __name__ == "__main__":
    app.run()
