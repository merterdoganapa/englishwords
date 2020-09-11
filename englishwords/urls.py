from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import registration
import words
from words import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',words.views.index,name= 'index'),
    path('user/',include('registration.urls')),
    path('word/',include('words.urls')),
]

urlpatterns += staticfiles_urlpatterns()
