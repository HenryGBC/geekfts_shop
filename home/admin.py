from django.contrib import admin
from .models import Shirt, Images, Size
# Register your models here.


@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex', 'type', 'price', 'description', 'slug')
	filter_horizontal = ('image', 'size')


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'color')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
	list_display = ('size', )