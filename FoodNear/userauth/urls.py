from django.urls import path
from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.index,name = "auth"),
    path('out/',views.out,name = "logout"),
    #path('../comments/<int:ind>',views.index,name = "index2")
]