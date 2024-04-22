from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializers , ASerializers , UserSerializer
from .models import Todo , a  
from rest_framework.views import APIView
from rest_framework import generics,mixins
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated




 #region function baseview 
@api_view(['GET'])
def todo_all(request : Request):
     if request.method == 'GET':
         todo_o=Todo.objects.all()
         todo_serializers=TodoSerializers(todo_o,many=True)
         return Response(todo_serializers.data,status.HTTP_200_OK)
     elif request.method == 'POST':
         serializer = TodoSerializers(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status.HTTP_201_CREATED)
     return Response(None,status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def aaa(request : Request):
    if request.method == 'GET':
        todo_o=a.objects.order_by('id').all().values().using('asd')
        todo_serializers=ASerializers(todo_o,many=True)
        return Response(todo_serializers.data,status.HTTP_200_OK)
@api_view(['GET' , 'PUT' , 'DELETE'])
def todo_all_edit_delete(request : Request ,todo_id : int):

    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response(None,status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serializer_get =TodoSerializers(todo)
        return Response(serializer_get.data,status.HTTP_200_OK)
    
    elif request.method=='PUT':
        serializer_put=TodoSerializers(todo ,data=request.data)
        if serializer_put.is_valid():
            serializer_put.save()
            return Response(serializer_put.data,status.HTTP_202_ACCEPTED)
        return Response(None,status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        todo.delete()
        return Response(None,status.HTTP_204_NO_CONTENT)
#endregion function base view

#region class baseview     
class TodoListDataApiView(APIView):

    def get(self,request:Request):
        todo_o=Todo.objects.order_by('id').all().values()
        todo_serializers=TodoSerializers(todo_o,many=True)
        return Response(todo_serializers.data,status.HTTP_200_OK)
    
    
    def post(self,request:Request):
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(None,status.HTTP_400_BAD_REQUEST)
    
class TodoSingleDataApiView(APIView):

    def get_object(self,todo_id:int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except Todo.DoesNotExist:
            return Response(None,status.HTTP_404_NOT_FOUND)

    def get(self,request: Request , todo_id:int):
        todo=self.get_object(todo_id)
        serializer_get =TodoSerializers(todo)
        return Response(serializer_get.data,status.HTTP_200_OK)


    def put(self,request: Request,todo_id:int ):
        todo=self.get_object(todo_id)
        serializer_put=TodoSerializers(todo ,data=request.data)
        if serializer_put.is_valid():
            serializer_put.save()
            return Response(serializer_put.data,status.HTTP_202_ACCEPTED)
        return Response(None,status.HTTP_400_BAD_REQUEST)


    def delete(self,request: Request , todo_id:int):
        todo=self.get_object(todo_id)
        todo.delete()
        return Response(None,status.HTTP_204_NO_CONTENT)
#endregion class base view
    

#region mixins view
class TodoListMixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Todo.objects.order_by('id').all()
    serializer_class=TodoSerializers

    def get(self,request:Request):
        return self.list(request)

    def post(self,request:Request):
        return self.create(request)
    
class TodoSingleMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Todo.objects.order_by('id').all()
    serializer_class=TodoSerializers

    def get(self,request:Request ,pk):
        return self.retrieve(request,pk)   

    def put(self,request:Request ,pk):
        return self.update(request,pk)

    def delete(self,request:Request ,pk):
        return self.destroy(request,pk)
#endregion mixins view  



#region generics 

            #PAGINATION
class GenericsApiViewPagination(PageNumberPagination):
    page_size=2
            
            #end pagination

class TodoGenericApiView(generics.ListCreateAPIView):
    queryset=Todo.objects.order_by('id').all()
    serializer_class=TodoSerializers
    pagination_class=GenericsApiViewPagination
    
class TodoDetailsGenericsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.order_by('id').all
    serializer_class=TodoSerializers
#endregion generics

#region viewsets
    
    #pagination offset
class ViewSetApiViewPagination(LimitOffsetPagination):
    page_size=3
    

#BasicAuthentication(احراز هویت)
class TodoViewSetApiView(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    pagination_class=ViewSetApiViewPagination
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
#endregion viewsets
    


    
#region generics relation
    #nested serializer or relation models
class UserGenericApiView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
#endregion generics relation



