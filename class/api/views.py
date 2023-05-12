from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books
from api.models import Reviews
from api.serializers import BookSerializer,ReviewSerializer
from rest_framework.viewsets import ViewSet
#class productsView(APIView):
 #   def get(self,request,*args,**kwargs):
        #return Response({"msg":"inside products get"})
#class MorningView(APIView):
    #def get(self,request,*args,**kwargs):
       # return Response({"msg":"Good morning"})

#class EveningView(APIView):
    #def get(self, request, *args, **kwargs):
       # return Response({"msg": "Godd Evening "})


#class AddView(APIView):
 #   def get(self,request,*args,**kwargs):
  #      num1=int(input("first number"))
   #     num2=int(input("second number"))
    #    res=num1+num2
     #   return Response({"result":res})

# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)+int(n2)
#         return Response({"res":res})

#
#
#
#
# class SubtractiveView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)-int(n2)
#         return Response({"res":res})
#

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({"result":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=1
        for i in range(1,(n+1)):
            res=res*i
        return Response(data=res)
             #OR

    #return Response({"rrsult":res})



class WorldcountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("text")
        words=txt.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)


class ProductView(APIView):
    def get(self,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)#deserilizer
        return Response(data=serializer.data)




    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)#**serilizer means ath dictonary ayitt print avan
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)#deserilizer
        return Response(data=serializer.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="delete")

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")#url ninn id ne extract cheyyunna thaan
        serializer=BookSerializer(data=request.data)#serilizer    :ivide data=koduth parayunnthuser ividdnn pass chyunna data kittunnth serilizer il aa data avidnn kittum
        if serializer.is_valid():#validath method call avunnth is_valid call avumbol aan aa method call avunth
            Books.objects.filter(id=id).update(**serializer.validated_data)#validated data ath tuple ayitt aan varunnth athine dictionary akkan aan **serilizer kodukkn
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class ReviewsView(APIView):
    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)#update aankil eth instance ann nne update chyynd enn ath object nne aanpinne nth data vechittan update chyynd ath user pass chyunna data vechittan aan  athan request.data kodukkn
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="delete")



#product view aam
        # return Response(data="inside details")
        # bname=request.data.get("name")
        # bauthor = request.data.get("author")
        # bprice = request.data.get("price")
        # bpublisher = request.data.get("publisher")
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
        # return Response(data="created")
        #


class ProductsViewsetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.filter(id=id)
        serializer=BookSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")





