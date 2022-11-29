'''Configurations for connecting to a MongoDB database'''
import os

from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()


def connect_database():
    '''Connects to the MongoDB database based on the environment variable'''
    conection_string = os.getenv("MONGODB_URI")
    connect(host=conection_string)
