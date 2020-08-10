from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import ListView
from django.urls import reverse

# Create your views here.
"""def index(request):
	return render(request, 'recommend.html')
"""

class Main(ListView):
	model = Book
	context_object_name = 'books'
	template_name = 'recommend.html'


def Search(request):
	search = request.GET.get('b_title')
	books_result = Book.objects.filter(name__icontains=search)
	if books_result == "<QuerySet []>":
		books_result = False
	return render(request, 'result.html', {'books_result': books_result})