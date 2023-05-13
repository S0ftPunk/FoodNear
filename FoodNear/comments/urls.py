from django.urls import path
from . import views
urlpatterns = [
    path('<place_id>/',views.index,name = "index2"),
    #path('<int>/',views.index,name = "index2"),
    # path('1/',views.index,name = "index2"),
    #path('<int:pk>/',views.CommentsOfPlace.as_view(),name = "index2"),
     path('leave_comment/<ind>/',views.leave_comment, name = "leave_comment")
]