import json
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://<username>:<password>@insertdataapi.umsi0.mongodb.net/')
db = client['employee_details']
collection = db['employee']

document = {
  "name": "Shivesh",
  "empID": "ANZ01",
  "address": "Bangalore"
}

@app.route('/employees', methods=['GET'])
def getAllEmployees():
  return jsonify(db["employee"])


@app.route('/employees', methods=['POST'])
def createEmployee():
   data = request.json
   collection.insert_one(data)

   return "Created a new emplpoyee"

# insert_doc = collection.insert_one(document)

# print("inserted document: {insert_doc}")

if __name__ == '__main__':
   app.run(port=5000)

client.close()