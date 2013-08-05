__author__ = 'kranthi'

from pymongo import MongoClient
import gridfs
import json

client = MongoClient('192.168.0.181')
dbname = 'sandiego'

class Parser_Form_Data:
    def __init__(self):
        self.title = ''
        self.website = ''
        self.parser = ''
        self.file = ''
        self.recipe = ''
        self.status = ''
        self.log = []



def store_parser_form_data(form_data, filestream=None):
    db = client[dbname]
    coll = db.parser_form_data
    rowid = coll.insert(form_data.__dict__)

    if not filestream == None:
        fs = gridfs.GridFS(db)
        print fs.put(filestream, filename=str(rowid) + "_" + form_data.file)


if __name__ == '__main__':
    dbname = 'sandiego_test'
    obj = Parser_Form_Data()
    obj.title = 'Chicken recipes'
    store_parser_form_data(obj, open('/Users/kranthi/Downloads/166160-chicken_prn.pdf', 'r'))
