from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('home/',views.wordsHome,name = "home"),
    path('foods/',views.wordsFoods,name = "food"),
    path('technology/',views.wordsTechnology,name = "technology"),
    path('general/',views.wordsGeneral,name = "general"),
    path('transportation/',views.wordsTransportation,name = "transportation"),
    path('verbs/',views.wordsVerbs,name = "verbs"),
    path('detail/<int:id>/',views.detail,name = "detail"),
    path('delete/<int:id>/',views.deleteWord,name = "delete"),
    path('myWords/',views.myWords,name = "myWords"), 
    path('addWord/home',views.addWord,name = "addWord"),
    path('addWord/food',views.addWord,name= "addWord"),
    path('addWord/technology',views.addWord,name ="addWord"),
    path('addWord/general',views.addWord,name = "addWord"),
    path('addWord/transportation',views.addWord,name = "addWord"),
]
