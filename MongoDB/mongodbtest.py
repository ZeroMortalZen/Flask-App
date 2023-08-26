import pymongo

print("connecting to db")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["products"]
products = db["products"]

buffer = '{"name":['

for x in products.find():
    # x is a dict
    if "item" in x:  # if the item att exists in x
        print(x["item"])
        buffer += '" ' + x['item'] + '  ",'

buffer = buffer[:-1]
buffer += ']}'

print(buffer)
