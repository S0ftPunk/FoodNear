from django.urls import path
from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.index,name = "main"),
    path('about/', views.about, name="about"),
    #path('../comments/<int:ind>',views.index,name = "index2")
]