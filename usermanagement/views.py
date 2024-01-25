from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizers import UserSerializer
from .models import User
from django.contrib import messages
# Create your views here.

@api_view(["GET"])
def listuser(request):
    user= User.objects.all()
    result = UserSerializer(user,many=True)
    return Response({"message":"From The Register page","user":result.data})


@api_view(["POST","GET"])
def createuser(request):
    if request.method=="POST":
        newuser=UserSerializer(data=request.data) 
        if newuser.is_valid(): 
            user=newuser.save()
            user.set_password(newuser.data.get("password"))
            user.save()
            return Response({"messages":"Sucess"})
        else:
            return Response({"messages":newuser.errors})
    return Response({"messages":""})

@api_view(["DELETE","GET"])
def deleteuser(request,pk):
    try:
        user=User.objects.get(id=pk)
        removeuser=UserSerializer(user)   
        if request.method=="DELETE":
            user.delete()
            return Response({"message":removeuser.data['email'] + " as been deleted"})
        return Response({"message":removeuser.data["email"]})
    except User.DoesNotExist:      
        return Response({"message":"user is not exist"})
            
@api_view(["PATCH","GET","PUT"])       
def updateuser(request,pk):
    pass