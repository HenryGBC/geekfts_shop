from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View, DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
from django.template.loader import render_to_string
import json
from django.conf import settings
from .models import Shirt, Order
import random


# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):

		shirts_model = Shirt.objects.all()[:5]
		shirts = []
		random_index = random.randint(0, 4)
		for shirt in shirts_model:
			shirt_data = {
				'name': shirt.name,
				'image': shirt.image.all()[0].image
			}
			shirts.append(shirt_data)


		context = super(IndexView, self).get_context_data(**kwargs)
		context.update({
			'shirts': shirts,
			'shirt_header': shirts[random_index]
		})

		return context


class GalleryView(TemplateView):

	template_name = "gallery.html"

	def get_context_data(self, **kwargs):

		shirts_model = Shirt.objects.all()
		shirts = []
		for shirt in shirts_model:
			shirt_data = {
				'name': shirt.name,
				'image': shirt.image.all()[0].image,
				'url': shirt.slug,
				'images': shirt.image.all()
			}
			shirts.append(shirt_data)


		context = super(GalleryView, self).get_context_data(**kwargs)
		context.update({
			'shirts': shirts
		})

		return context


class ShirtDetail(DetailView):
    template_name = 'detail.html'
    model = Shirt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OrderView(TemplateView):
	template_name = 'order.html'

	def get_context_data(self, **kwargs):

		number = self.request.GET.get('number', None)
		email = self.request.GET.get('email', None)
		print('NUMBEERR', number)
		print('EMAIILL', email)
		context = super(OrderView, self).get_context_data(**kwargs)
		try:
			order = Order.objects.get(number=number, email=email)
			products = []
			for product in order.product.all():
				image_color = ''
				for image in product.shirt.image.all():
					if image.color == product.color:
						image_color = image
				data_product = {
					'shirt': product.shirt,
					'quantity': product.quantity,
					'image': image_color
				}

				products.append(data_product)


			context.update({
				'order': order,
				'products': products,
				'valid': True
			})


		except Order.DoesNotExist:
			context.update({
				'order': '',
				'products': [],
				'valid': False
			})
		return context


