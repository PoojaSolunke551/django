from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router= DefaultRouter()
router.register('api',views.BlogPostView,basename = 'blogpost')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)) ,

    path('gettoken/',TokenObtainPairView.as_view(),name='TokenObtain') ,
    path('refreshtoken/',TokenRefreshView.as_view(),name='TokenRefresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='TokenVerify'),

    path('dj-rest-auth/',include('dj_rest_auth.urls')),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path ( 'dj-rest-auth/facebook/', views.FacebookLogin.as_view ( ), name = 'fb_login' )     # Facebook login
]