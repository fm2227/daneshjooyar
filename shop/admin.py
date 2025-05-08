from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'quantity', 'status']
    search_fields = ['title']
    list_filter = ['status']

    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'quantity']

    def delete_queryset(self, request, queryset):
        for cart in queryset:
            cart.delete()


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'status']
    list_filter = ['status']

    def delete_queryset(self, request, queryset):
        for order in queryset:
            order.delete()


@admin.register(models.OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'product', 'quantity', 'price']

    def delete_queryset(self, request, queryset):
        for orderproduct in queryset:
            orderproduct.delete()
