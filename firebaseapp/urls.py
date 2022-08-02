from django.urls import path
from .views import CreateListTodoView, TodoView, UpdateTodoView
urlpatterns = [
    path('todos', CreateListTodoView.as_view()),  
    path('todo/<str:id>', TodoView.as_view()),  
    path('updatetodo/<str:id>', UpdateTodoView.as_view()),  
    
    
   
]
  