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
        a = 2
        b = 2
        # updateInventory = "UPDATE products SET qtyInStock = qtyInStock - " +  str(a) +") WHERE productID = " + str(b)

        curs = db.cursor()
        app.logger.info("****************Order id****************::" + str(orderID))
        for row in result_set:
          
        #     app.logger.info("***********")
        #     app.logger.info("row0::")
        #     app.logger.info(row[0])

        #     app.logger.info("row1::")
        #     app.logger.info(row[1])
        #     app.logger.info("***********")
        #     app.logger.info(row)
            updateInventory = "UPDATE products SET qtyInStock = (qtyInStock - " +  str(row[1]) + ") WHERE productID = " + str(row[0])
            # updateInventory = "UPDATE products SET qtyInStock = (qtyInStock - %d) WHERE productID = %d".format(int(row[1]), int(row[0]))
            curs.execute(updateInventory)
            db.commit()
        #     app.logger.info(updateInventory)
        #     app.logger.info(curs.execute(updateInventory))

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