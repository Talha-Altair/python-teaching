import math

a = math.cos(0)

# print(a)

# import datetime

# c  = datetime.datetime.now()

# d = c.weekday() 

# print(d)

import json

data = {
    "day" : "thursday",
    "score": 10
}

a = json.dumps(data)

print(type(a))

c = json.loads(a)

print(type(c))

# print(json.dumps(data))