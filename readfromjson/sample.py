from json import load
with open("bikes.json") as f:
    data=load(f)
#print(data)


bikes_name=[bike.get("name") for  bike in data]
print(bikes_name)
costly_bike=max(data,key=lambda b:b.get("price"))
print(costly_bike)


red_bikes=[bike.get("name") for bike in data if "red" in  bike.get("colors")]
print(red_bikes)