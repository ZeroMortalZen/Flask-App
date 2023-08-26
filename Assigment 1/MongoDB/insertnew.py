import pymongo

print("connecting to db")

myclient = pymongo.MongoClient("mongodb://localhost:27017")

db = myclient["products"]  # select the db
products = db["products"]  # select the collection

prod_list = [
    {"code": "234", "item": "arm_rest", "qty_in_stock": "1", "unit_price": "40.50"},
    {"code": "1351", "item": "Bench seat", "qty_in_stock": "4", "unit_price": "20.50"},
    {"code": "453411", "item": "Bucket seat", "qty_in_stock": "4", "unit_price": "5.10"},
    {"code": "7811", "item": "Children and baby car seat", "qty_in_stock": "5", "unit_price": "20.50"},
    {"code": "13231", "item": "Fastener", "qty_in_stock": "2", "unit_price": "20.10"},
    {"code": "23411", "item": "Headrest", "qty_in_stock": "5", "unit_price": "22.10"},
    {"code": "11", "item": "Seat belt", "qty_in_stock": "10", "unit_price": "120.10"},
    {"code": "181", "item": "Seat bracket", "qty_in_stock": "22", "unit_price": "34.10"},
    {"code": "711", "item": "Seat cover", "qty_in_stock": "30", "unit_price": "230.10"},
    {"code": "14561", "item": "Seat track", "qty_in_stock": "50", "unit_price": "23.10"},
    {"code": "1134", "item": "Other seat components", "qty_in_stock": "2", "unit_price": "20.10"},
    {"code": "11311", "item": "Back seat", "qty_in_stock": "10", "unit_price": "202.10"},
    {"code": "234234", "item": "Front seat", "qty_in_stock": "11", "unit_price": "210.510"}




]

x = products.insert_many(prod_list)
print(x.inserted_ids)
