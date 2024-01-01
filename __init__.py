from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randomString'
    CORS(app)

    client = MongoClient("mongodb+srv://fangjun0616:passwordis040616011151@cluster0.swnk2hb.mongodb.net/?retryWrites=true&w=majority")

    app.config['MONGO_CLIENT'] = client

    from routes import main
    app.register_blueprint(main)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)