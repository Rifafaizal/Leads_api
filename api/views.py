from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from rest_framework.response import Response

class BookListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        context={"message":"this is book list view"}
        return Response(data=context)

    def post(self,request,*args,**kwargs):
        context={"message":"this is book create view"}
        return Response(data=context)  


class BookRetrieveDeleteUpdateView(APIView):
    def get(self,request,*args,**kwargs):
        context={"message":"this is list get or retrieve view"}
        return Response(data=context)

    def put(self,request,*args,**kwargs):
        context={"message":"this is book update view "}  
        return Response(data=context)

    def delete(self,request,*args,**kwargs):
        context={"message":"this is book delete view"}
        return Response(data=context)



# API---ENABLES COMMUNICATION BTETWEEN 2 SOFTWARE APPLIOCATIONS


# http_request:
    # url:
    # method:get,post,put/patch,delete
    # body:
    # headers:

# json-format of transfering data
# DRF
# rest_framework>views>ApiView
# rest_framework>response>Response       
# Response=python native format-->json files
# 
