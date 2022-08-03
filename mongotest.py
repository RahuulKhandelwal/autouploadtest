import pymongo
client = pymongo.MongoClient("mongodb+srv://RahuulFirstMongodb:rahuulmongodb123@cluster0.gcjgv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={'name':'Rahuul','email_id':'khandelwal.rahuul@mail.com','surname':'Khandelwal'
}
db1=client['mongotest1']
coll=db1['test']
coll.insert_one(d )