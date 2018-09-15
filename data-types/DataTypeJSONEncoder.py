import json
class DataTypeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'toJSON'):
            return obj.toJSON()
        else:
            return json.JSONEncoder.default(self, obj)
    
#TO serialize just say json.dumps(myobj,cls=DataTypeJSONEncoder)    

# THIS IS THE WAY FOR DESERIALIZING IF NEEDED WE WRITE OUR OWN OBJECT HOOK AND USE json.loads
    
# def decodeobj(o):
#     print("o has",o)
#     if "car" in o:
#         car=Car()
#         car.carType=o["car"]["carType"]
#         car.carId=o["car"]["carId"]
#         car.carModel=o["car"]["carModel"]
#         car.carLicense=o["car"]["carLicense"]
#         t=test()
#         t.name=o["name"]
#         t.age=o["age"]
#         t.car=car
#         return t
#     return o

# a=json.loads(ser,object_hook=decodeobj)
# print(a)
# ser1=json.dumps(a.toJSON(),cls=CarEncoder)
# print(ser1)