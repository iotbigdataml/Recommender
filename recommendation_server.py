from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from json import dumps, loads, load
import http.client, urllib, urllib.request, urllib.parse, urllib.error, base64, re, json, pymysql
import requests

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.debug = True

db = pymysql.connect(host="ediss.cj2pus6demaz.us-east-1.rds.amazonaws.com", user="root", passwd="admin123", db="login")

class Notify(Resource):
    def get(self):
        self.createPallets(self.readDB())
        #strjson = '[{\"orderid\":1,\"item\":\"Blue\",\"inventory\":9},{\"orderid\":2,\"item\":\"Red\",\"inventory\":3},{\"orderid\":3,\"item\":\"Yellow\",\"inventory\":4}]'
        #return strjson
        return "noted"
    
    def post(self):
        return "Processed"

    def readDB(self):
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
        r = requests.get(url)
        return r
    
    def createPallets(self,orders):
        #intelligent logic goes here
        #for(order:orders)
            #insertQuery = ""
            #cursor = db.cursor()
            #result  = cursor.execute(insertQuery)
            #db.commit()
        return "pallets"

class GetPallet(Resource):
    def get(self):
        return getPallet()
    
    def post(self):      
        return "Processed"

def getPallet():
        print(db)
        cursor = db.cursor()
        sql = "select * from account"
        print(cursor.execute(sql))
        rows = cursor.fetchall()
        print(type(rows))
        # Convert query to row arrays
        rowarray_list = []
        # for row in rows:
        #     rowarray_list.append(row)
        orderid = 123 #get from rows
        markread(orderid)
        return json.dumps(rows)

def markread(orderid):
        print(orderid)
         
api.add_resource(Notify, '/notify') # Route_1
api.add_resource(GetPallet, '/getpallet') # Route_2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, threaded=True)
