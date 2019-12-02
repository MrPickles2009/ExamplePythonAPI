from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import socket

db_connect = create_engine('sqlite:///VehicleInfo.db')
app = Flask(__name__)
api = Api(app)

class Vehicles(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from Vehicles") # This line performs query and returns json result
        result = {'Vehicles': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    def post(self):
        conn = db_connect.connect() # connect to database
        req = request.get_json()
        newData = req['newData']
        makeName = newData['makeName']
        maxSpeed = newData['maxSpeed']
        modelName = newData['modelName']
        modelYear = newData['modelYear']

        query = "insert into Vehicles values (null, \"" + makeName + "\", \"" + modelName + "\", " + str(modelYear) + ", " + str(maxSpeed) + ")"
        conn.execute(query)

        return "Vehicles data updated"

class GetVehicle(Resource):
    def get(self, vehicle_id):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from Vehicles where id = %d " %int(vehicle_id)) # This line performs query and returns json result
        result = {'Vehicle': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class DeleteVehicle(Resource):
    def get(self, vehicle_id):
        conn = db_connect.connect() # connect to database
        query = conn.execute("delete from Vehicles where id = %d " %int(vehicle_id)) # This line performs query and returns json result
        return "Vehicle deleted"

api.add_resource(Vehicles, '/vehicles')
api.add_resource(GetVehicle, '/getvehicle/<vehicle_id>')
api.add_resource(DeleteVehicle, '/deletevehicle/<vehicle_id>')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers',
                       'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods',
                       'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    hostname = socket.gethostname()
    dns_resolved_addr = socket.gethostbyname(hostname)
    print(str(dns_resolved_addr))
    app.run(host=str(dns_resolved_addr), port=8080)
