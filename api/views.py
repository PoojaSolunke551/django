from django.shortcuts import render
from .models import User,BlogPost
from .serialization import UserSerializer,BlogPostSerializer
from rest_framework.viewsets import ModelViewSet
from .pagination import MyPageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here.'

class BlogPostView(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class =MyPageNumberPagination
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]




class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter