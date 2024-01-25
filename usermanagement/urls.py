from django.urls import path
from .views import listuser,createuser,deleteuser,updateuser
urlpatterns=[
    path("listuser/",listuser,name="listuser"),
    path("create/",createuser,name="create"),
    path("update/<int:pk>/",updateuser,name="update"),
    path("delete/<int:pk>/",deleteuser,name="delete"),
]