from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.createBook,name='createbok'),
 path('',views.listBook,name='booklist'),
 path('update/<int:book_id>/',views.updateBook, name='update'),
 path('detailsview/<int:book_id>/',views.detailsView, name='details'),
 path('delete/<int:book_id>/',views.deleteView, name='delete'),
 
 path('author/',views.createauthor, name='author'),
 path('index/',views.index),
 path('search/',views.searchBook, name='search')
]
