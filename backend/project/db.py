from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_db():
    try:
        uri = "mongodb+srv://databaseUser:ZTfN0nyd8oSsaNs4@cluster0.3i13gxn.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None


