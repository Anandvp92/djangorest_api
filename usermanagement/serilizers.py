from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields = ["email","phonenumber","profile_image","full_name"]
        #exclude = ("last_login","date_joined","password","groups","user_permissions")