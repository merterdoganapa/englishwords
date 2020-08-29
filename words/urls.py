from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('home/',views.wordsHome,name = "home"),
    path('foods/',views.wordsFoods,name = "food"),
    path('detail/<int:id>/',views.detail,name = "detail"),
    path('delete/<int:id>/',views.deleteWord,name = "delete"),
    path('myWords/',views.myWords,name = "myWords"), 
    path('addWord/home',views.addWord,name = "addWord"),
    path('addWord/food',views.addWord,name= "addWord"),
    
]
