from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from json import dumps, loads, load
import http.client, urllib, urllib.request, urllib.parse, urllib.error, base64, re, json, pymysql, requests

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.debug = True

fulfillmentServiceurl = ""
class Notify(Resource):
    def get(self):
        self.createPallets(self.readDB())
        return "noted"
    
    def post(self):
        return "Processed"

    def readDB(self):
        rows = ""
        return rows #modify this
    
    def createPallets(self,orders):
        #intelligent logic goes here
        # call insert API from Orer fulfillment
        return "pallets"

class GetPallet(Resource):
    def get(self):
        return getPallet()
    
    def post(self):      
        return "Processed"

def getPallet():
        #implement if needed
        return "NOT IMPLEMENTED"

def markread(orderid):
        print(orderid)
         
api.add_resource(Notify, '/notify') # Route_1
api.add_resource(GetPallet, '/getpallet') # Route_2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, threaded=True)
