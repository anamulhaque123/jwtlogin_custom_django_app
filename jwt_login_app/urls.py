from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path('token/',TokenObtainPairView.as_view()),
    path('custom-token/',MyTokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),   #not mandatory
    path('registration/', registrationAPI)
]