import os
from sqlalchemy import create_engine, text
from pymongo import MongoClient


MYSQL_URL = os.getenv("MYSQL_URL")
MONGO_URL = os.getenv("MONGO_URL")


class CompCraftSQL:
    engine = create_engine(MYSQL_URL)

    def __init__(self):
        self.engine = create_engine(MYSQL_URL)

    def execute(self, query: str, values=[]):
        data = []
        with self.engine.connect() as con:
            result = con.execute(
                text(query),
                values,
            )
            for row in result:
                data.append(row)
            con.close()
        return data


class CompCraftMONGO:
    # client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
    client = MongoClient(MONGO_URL)

    def __init__(self):
        self.database = self.client.compcraft

    def enchantments(self):
        return self.database.get_collection('enchantments')

    def shops(self):
        return self.database.get_collection('shops')

    def jobs(self):
        return self.database.get_collection('jobs')

    def talismans(self):
        return self.database.get_collection('talismans')
