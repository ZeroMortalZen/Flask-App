import requests
from flask import Flask, jsonify
from flask_restful import Resource, Api
import pymongo
from flask_restful.representations import json
import mysql.connector

app = Flask(__name__)
api = Api(app)

# Establish a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="example",
    database="db"
)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


# getStockIDs endpoint
class getStockIDs(Resource):
    def get(self):
        outputBuffer = '{"code": ['  # put all the content to send back

        file1 = open("products.txt", "r")  # open file
        content = file1.readlines()  # getting the lines
        for line in content:  # for each line # x is each line
            # print(line)
            prodCode = line.split('-')  # splitting the line and turns line into an array everywhere it finds a
            # line#turns line into
            # an array
            print(prodCode[0])  # just give first element in array at position 0

            # For every product code,make a new element in the buffer of JSON
            outputBuffer += '' + prodCode[0] + ','
        outputBuffer += '666]}'
        print(outputBuffer)
        import json

        return json.loads(outputBuffer)


api.add_resource(getStockIDs, '/getStockIDs')


class getStockNames(Resource):
    def get(self):
        print("connecting to db")

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        db = myclient["products"]
        products = db["products"]

        buffer = '{"name":['

        for x in products.find():
            # x is a dict
            if "item" in x:  # if the item att exists in x
                print(x["item"])
                buffer += '" ' + x['item'] + '  ",'

        buffer = buffer[:-1]
        buffer += ']}'

        print(buffer)

        return buffer


api.add_resource(getStockNames, '/getStockNames')


class getQty(Resource):
    def get(self):
        url = "http://localhost:4000/jsonrpc"
        headers = {'content-type': 'application/json'}

        # Example echo method
        payload = {
            "method": "getQty",
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()

        # printing the response
        print(response["result"])


api.add_resource(getQty, '/getQty')


class getAllData(Resource):
    def get(self):
        # Establish a MySQL connection
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="yourpassword",
            database="yourdatabase"
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute a SQL query
        cursor.execute("SELECT * FROM products")

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Convert the rows to a dictionary
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'products': row[1],
                'qty': row[2],
                'price': row[3],
            })

        # Return the data as a JSON response
        return jsonify(data)


api.add_resource(getAllData, '/getAllData')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
