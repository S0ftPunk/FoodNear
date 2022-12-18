from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('/leave_comment/',views.leave_comment, name = "leave_comment")
]