from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
uri = "mongodb+srv://vaidik:12345@cluster0.vcctw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create new client and connect to server

client = MongoClient(uri)

#database name and collection name

DATABASE_NAME = "Vaidik_"
COLLECTION_NAME = "WaferFault"

df = pd.read_csv("C:\Project/notebooks\wafer_23012020_041211.csv")

df =df.drop("Unnamed: 0", axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)