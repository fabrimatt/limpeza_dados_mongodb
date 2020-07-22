#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import codecs
from pymongo import MongoClient

FILE = "/Users/fabriciomattos/Documents/udacity/mongo_db/rj.osm.json"



if __name__ == "__main__":
    
   

    client = MongoClient("mongodb://localhost:27017")
    
    db = client['rj']
    collection = db['rj_city']

    data = json.load(open(FILE))
    db.rj.insert(data) 
    print db.rj.find_one()