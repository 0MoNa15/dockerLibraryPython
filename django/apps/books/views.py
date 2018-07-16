from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
	"""
		Aqui va un comentario explicativo de la clase
	"""

	template_name = "index.html"

class CreateBooks(TemplateView):
	template_name = "books/create_books.html"