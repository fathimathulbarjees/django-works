from django.shortcuts import render

# Create your views here


from rest_framework.views import APIView

from rest_framework.response import Response

class productsView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"inside products get"})

