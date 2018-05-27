from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.template.loader import render_to_string
import json
from django.conf import settings
from .models import Shirt
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
				'image': shirt.image.all()[0].image
			}
			shirts.append(shirt_data)


		context = super(GalleryView, self).get_context_data(**kwargs)
		context.update({
			'shirts': shirts
		})

		return context