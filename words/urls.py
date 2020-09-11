from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "words"

urlpatterns = [
    path('home/',views.wordsHome,name = "home"),
    path('foods/',views.wordsFoods,name = "food"),
    path('technology/',views.wordsTechnology,name = "technology"),
    path('general/',views.wordsGeneral,name = "general"),
    path('transportation/',views.wordsTransportation,name = "transportation"),
    path('verbs/',views.wordsVerbs,name = "verb"),
    path('detail/<int:id>/',views.detail,name = "detail"),
    path('delete/<int:id>/',views.deleteWord,name = "deleteWord"),
    path('update/<int:id>',views.updateWord,name = "updateWord"),
    path('myWords/',views.myWords,name = "myWords"), 
    path('addWord/home',views.addWord,name = "addHome"),
    path('addWord/food',views.addWord,name= "addFood"),
    path('addWord/technology',views.addWord,name ="addTechnology"),
    path('addWord/general',views.addWord,name = "addGeneral"),
    path('addWord/transportation',views.addWord,name = "addTransportation"),
    path('addWord/verb',views.addWord,name = "addVerb"),
    path('deleteComment/<int:id>',views.deleteComment,name = "deleteComment"),
    path('updateComment/<int:id>',views.updateComment,name = "updateComment"),
]
