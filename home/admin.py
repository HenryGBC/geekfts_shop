from django.contrib import admin
from .models import Shirt, Images, Size, ShirtOrder, Order
# Register your models here.


@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex', 'type', 'price', 'description', 'slug')
	search_fields = ('name',)
	filter_horizontal = ('image', 'size')


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'color')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
	list_display = ('size', )


@admin.register(ShirtOrder)
class ShirtColorAdmin(admin.ModelAdmin):
	list_display = ('shirt', 'color', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'status', 'total', 'iva', 'number', 'address')
	search_fields = ('name', 'email', 'status', 'phone')
	filter_horizontal = ('product',)











