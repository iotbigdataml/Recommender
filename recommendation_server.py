from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps, loads, load
import http.client, urllib.request, urllib.parse, urllib.error, base64, re
import pandas as pd

app = Flask(__name__)
api = Api(app)

app.debug = True

class Notify(Resource):
    def get(self):
        request.args.get('a')
        self.readDB()
        self.createPallets()
        return "noted"
    
    def post(self):
        return "Processed"

    def readDB(self):
        return "read"
    
    def createPallets(self):
        return "pallets"

class GetPallet(Resource):
    def get(self):
        return "getpallet"
    
    def post(self):      
        return "Processed"

def process(desc,desc_name):
        df=pd.read_json(desc)
        print(df)
        filename = desc_name + ".csv"
        df.to_csv(filename, encoding='utf-8', index=False)
         
api.add_resource(Notify, '/notify') # Route_1
api.add_resource(GetPallet, '/getpallet') # Route_2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, threaded=True)