from pymongo import MongoClient

# basic mongodb CRUD operations. 

def get_db(db_name):
    db = db_name
    return db

def create_db():
    client = MongoClient('localhost:27017')
    db = client.my_database
    return db

def add_row(db):
    document_json = {}
    document_json['name'] = "karan"
    document_json['number'] = 123456789
    # print document
    print(document_json)
    # inserting document in table
    db.collection.insert(document_json)

if __name__ == "__main__":
    my_db = create_db
    add_document(my_db)
    print(get_db.collection.find_all())
   
