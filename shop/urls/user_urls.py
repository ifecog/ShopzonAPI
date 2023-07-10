from django.urls import path, include
from rest_framework import routers
from shop.views.user_views import UserViewSet, MyTokenObtainPairView

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/login/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('register/', UserViewSet.as_view({'post': 'register_user'}), name='register-user'),
]