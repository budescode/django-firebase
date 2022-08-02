import os
from helpers.helpers import db
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import TodoSerializer
import firebase_admin

class CreateListTodoView(generics.ListCreateAPIView):    
    serializer_class = TodoSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():            
            name = serializer.validated_data['name']
            description = serializer.validated_data['description']
            doc_ref = db.collection(f'todolist')
            added_data = doc_ref.add({
                f'name': f'{name}',
                f'description': f'{description}',
                f'timestamp':firebase_admin.firestore.firestore.SERVER_TIMESTAMP            
            })   
            response_id = added_data[1].get().id
            response_data = added_data[1].get().to_dict()
            response_data['id']=response_id 
            print(response_data)
            data = {'message':'successfully created'}
            return Response(data, status=HTTP_201_CREATED)
        else:
            data = {"message":serializer.errors}
            return Response(data, status=HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        doc_ref = db.collection(u'todolist').get()
        #print(doc_ref[0].to_dict())
        return []


class TodoView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer
    def get(self, request, id, format=None):
        doc_ref = db.collection(f'todolist').document(id)
        doc = doc_ref.get()
        data = doc.to_dict()         
        return Response(data)

    def delete(self, request, id, format=None):
        doc_ref = db.collection(f'todolist').document(id)
        doc_ref.delete()  
        return Response({}, status=HTTP_204_NO_CONTENT)


class UpdateTodoView(generics.CreateAPIView):    
    serializer_class = TodoSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def patch(self, request, id, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():            
            name = serializer.validated_data['name']
            description = serializer.validated_data['description']
            doc_ref = db.collection(f'todolist').document(id)
            added_data = doc_ref.update({
                f'name': f'{name}',
                f'description': f'{description}',
                            
            })   
            print(added_data)
            return Response({'message':'success'}, status=HTTP_201_CREATED)
        else:
            data = {"message":serializer.errors}
            return Response(data, status=HTTP_400_BAD_REQUEST)