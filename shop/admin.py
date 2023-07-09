from django.contrib import admin
from .models import (
    Category, 
    Brand, 
    Product, 
    Review,
)
from django.utils.html import format_html

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name']

class BrandAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('_id', 'thumbnail', 'name', 'category', 'brand')
    list_filter = ('category', 'brand')
    list_display_links = ('name', 'thumbnail')
    search_fields = ['name', 'description', 'brand', 'category']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'rating', 'created_time')
    list_display_links = ['name']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
