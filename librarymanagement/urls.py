from django.contrib import admin
from django.urls import path,include
from librarymanagement import views

urlpatterns = [

    path('',views.index,name='library'),
    path('about',views.about,name='about'),
    path('books',views.books,name='books'),
   
]