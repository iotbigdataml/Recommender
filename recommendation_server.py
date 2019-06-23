from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from json import dumps, loads, load
import http.client, urllib, urllib.request, urllib.parse, urllib.error, base64, re, json, pymysql, requests

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.debug = True


db = pymysql.connect(host="localhost", user="root", passwd="password", db="iot")

class Notify(Resource):
    def get(self):
        return "NOT IMPLEMENTED!"
    
    def post(self):
        orderID = request.get_json()["orderID"]
        selectProdIDQty = "SELECT productID, qtyOrdered FROM orderProducts WHERE orderID =" + str(orderID)
        cursor = db.cursor()
        cursor.execute(selectProdIDQty)
        result_set = cursor.fetchall()

        for row in result_set:
            curs = db.cursor()
            print("%s, %s" % (row["productID"], row["qtyOrdered"]))
            updateInventory = "UPDATE products SET qtyInStock = qtyInStock - "+  row["qtyOrdered"] +" WHERE productID = " + row["productID"]
            curs.execute(updateInventory)

        return "Updated"

class GetPallet(Resource):
    def get(self):
        return getPallet()
    
    def post(self):      
        return "NOT IMPLEMENTED!"

def getPallet():
        #implement if needed
        return "NOT IMPLEMENTED!"

def markread(orderid):
        print(orderid)
         
api.add_resource(Notify, '/notify') # Route_1
api.add_resource(GetPallet, '/getpallet') # Route_2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, threaded=True)