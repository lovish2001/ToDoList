from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo


app = Flask(__name__)
app.secret_key = "31bfa1d3aa732e00e9796cbcdd880df45b902a9d"
client = pymongo.MongoClient("mongodb+srv://kumarlovish0000:root@cluster0.mqn2aan.mongodb.net/?retryWrites=true&w=majority")


# mongodb database
# mongodb_client = PyMongo(app)
# db = mongodb_client.db
db = client.get_database('TodoLIST')
from application import routes