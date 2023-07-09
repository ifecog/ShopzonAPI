from django.urls import path, include
from rest_framework import routers
from shop.views.product_views import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/', ProductViewSet.as_view({'get':  'get_product_details'}), name='product-details'),
    # path('products/toprated/', ProductViewSet.as_view({'get':  'get_toprated_products'}), name='top-rated-products'),
]