from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.template.loader import render_to_string
import json
from django.conf import settings


# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"