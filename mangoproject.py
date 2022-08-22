import pymongo
import math
from urllib.parse import quote_plus

username = quote_plus('ddsprasad')
password = quote_plus('Apple@99')
cluster = 'cluster0.rkbaq8g.mongodb.net'


print(math.floor(2.93))


uri = "mongodb://"+username+":"+password+"@ac-6elyuxm-shard-00-00.rkbaq8g.mongodb.net:27017,ac-6elyuxm-shard-00-01.rkbaq8g.mongodb.net:27017,ac-6elyuxm-shard-00-02.rkbaq8g.mongodb.net:27017/?ssl=true&replicaSet=atlas-7r359z-shard-0&authSource=admin&retryWrites=true&w=majority"
# uri = 'mongodb://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'

client = pymongo.MongoClient(uri)

# result = client["sample_airbnb"]["listingsAndReviews"].find()
result = client["sample_airbnb"]["listingsAndReviews"].find_one()



print(result)

# # print results
# for i in result:
#     print(i)
