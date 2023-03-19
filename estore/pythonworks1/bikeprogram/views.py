from bikeprogram.models import bikes
class Bikes:
    def list(self,*args,**kwargs):
        return bikes

    def retrieve(self,*args,**kwargs):
        code=kwargs.get("code")
        bike=[b for b in bikes if b.get("code")==code]
        return bikes
    def create(self,*args,**kwargs):
        bike=kwargs.get("data")
        bikes.append(bike)
        return bike
    def update(self,*args,**kwargs):
        code=kwargs.get("code")
        data=kwargs.get("data")
        instance=[b for b in bikes if b.get("code")==code][0]
        instance.update(data)
        return instance
    def destroy(selfs,*args,**kwargs):
        code=kwargs.get("code")
        instance=[b for b in bikes if b.get("code")==code][0]
        bikes.remove(instance)
        return instance
b=Bikes()
#data={"code":1002,"name":"hynes","colors":["red","blue","grey","white"],"price":260000,"brand":"honda","fuel-type":"petrol"}
#print(b.update(code=1002,data=data))
print(b.destroy(code=1002))

#print(b.list())
#print(b.retrieve(code=1000))
#data={"code":1006,"name":"ray",
     # "colors":["red","white"],
      #"price":100000,"brand":"yellow",
      #"fueal-type":"petrol"}
#print(b.create(data=data))
#print(b.list())