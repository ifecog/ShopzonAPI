from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from shop.models import Brand, Category, Product, Review
from shop.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(ModelViewSet):
    # queryset = get_list_or_404(Product)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        category_id = self.request.query_params.get('category')
        brand_id = self.request.query_params.get('brand')
        
        query = self.request.query_params.get('keyword')
        if not query:
            query = ''
        
        queryset = queryset.filter(name__icontains=query)
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if brand_id:
            queryset = queryset.filter(brand_id=brand_id)
            
        return queryset
    
    def get_paginated_response(self, queryset):
        page = self.request.query_params.get('page')
        paginator = Paginator(queryset, 8)
        
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
            
        return Response({
            'products': self.serializer_class(products, many=True).data,
            'page': page,
            'pages': paginator.num_pages
        })
        
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        return product
    
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = self.serializer_class(product, many=False)
        return Response(serializer.data)
            
        
        