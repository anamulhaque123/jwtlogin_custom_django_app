from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.





@api_view(['POST',])
def registrationAPI(request):
    if request.method == "POST":
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

        # check already username
        if User.objects.filter(username=username).exists():
            return Response({"error": "An user with that username already exists!"})
        
        # match password
        if password1 != password2:
            return Response({"error": "Password didn't match"})
        
        # initial work
        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True   # Otherwise login is not possible

        user.set_password(raw_password=password1)   #password are not visible
        user.save()
        return Response({"success": "User successfully registered"})





# this for customize simple jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['type'] = "Bearer"
        data['lifetime'] = str(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
