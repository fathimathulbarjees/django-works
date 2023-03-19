from json import load
with open("bikes.json") as f:
    data=load(f)
#print(data)

#bike name
bike_name=[bike.get("name") for bike in data]
#print(bike_name)

#costly bike

costly_bike=max(data,key=lambda b:b.get("price"))
#print(costly_bike)


#for bike in data:
   # if "red" in bike.get("colors"):
      #  print(bike.get("name"))


red_bike=[bike.get("name")for bike in data if "red" in bike.get("colors")]
print(red_bike)



