import pymongo
from pymongo import MongoClient
from bson import ObjectId

from flask import Flask, Blueprint, jsonify, request, current_app
from flask_cors import CORS

main = Blueprint('main', __name__)

@main.route('/', methods = ["GET"])
def show():
    try:
        if request.method == "GET":
            return "Hello Backend", 201
    except Exception as e:
        print(f"Error:{e}")
        return "Error", 404

@main.route('/main/about_me', methods=['POST', 'GET'])
def about_me():
    try:
        # Retrieve MongoDB client from the app configuration
        client = current_app.config['MONGO_CLIENT']

        # Ensure that the client is not None
        if client is not None:
            # Retrieve or initialize the MongoDB collection
            db = client.get_database('Cluster0')
            collection = db.get_collection('MyCluster')

            print(f"Collection: {collection}")
            print(f"Database Name: {db.name}")
            print(f"Collection Name: {collection.name}")

            # Check if the collection is not None
            if collection is not None:
                # Rest of your route handling code...

                if request.method == "POST":
                    # Ensure the client and collection are initialized before using them
                    if client is not None and collection is not None:
                        details = {
                            "Name": "Lim Fang Jun",
                            "Course": "Math",
                            "Year": "Year 1",
                            "List all your CCA's": "Road Relays, RHDevs, SETS"
                        }

                        # Insert the details into the MongoDB collection
                        result = collection.insert_one(details)

                        # Check if the insertion was successful
                        if result.inserted_id:
                            details['_id'] = str(result.inserted_id)
                            return jsonify(details), 201
                        else:
                            return "Failed to insert data into the database", 500

                elif request.method == "GET":
                    # Handle GET request to retrieve data based on the 'Name' parameter
                    name_param = request.args.get('Name')

                    if name_param:
                        # Ensure the client and collection are initialized before using them
                        if client is not None and collection is not None:
                            # Query the database based on the 'Name' parameter
                            result = collection.find_one({"Name": name_param})

                            if result:
                                result['_id'] = str(result['_id'])
                                return jsonify(result), 200
                            else:
                                return "Data not found for the provided Name", 404
                        else:
                            return "MongoDB client or collection not initialized", 500
                    else:
                        return "Name parameter is missing in the request", 400
                return jsonify({"message": "Success"}), 200
            else:
                return "MongoDB collection not found", 500

        else:
            return "MongoDB client not initialized", 500

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return "Internal Server Error", 500
    



  
            


    