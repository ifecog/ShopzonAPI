from django.urls import path, include
from rest_framework import routers
from shop.views.user_views import UserViewSet, MyTokenObtainPairView

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view())
    # path('products/toprated/', ProductViewSet.as_view({'get':  'get_toprated_products'}), name='top-rated-products'),
]