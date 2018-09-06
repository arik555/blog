from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
def home(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs, }
	return render(request, 'blogs/index.html', context)


def detail(request, id=None):
	instance = Blog.objects.get(id=id)
	context = {'instance': instance, }
	return render(request, 'blogs/detail.html', context)

def update(request, id=None):
	if not request.user.is_authenticated:
		raise Http404
	instance = Blog.objects.get(id=id)
	if request.method == 'POST':
		form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Update Success.')
			return redirect('blog_detail', id=id)
	else:
		form = BlogForm(instance=instance)
	context = { 'form': form, }
	return render(request, 'blogs/update.html', context)

def add(request):
	if not request.user.is_authenticated:
		raise Http404
	if request.method == 'POST':
		form = BlogForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.add_message(request, messages.SUCCESS, 'Add Success.')
			return redirect('blog_detail', id=instance.id)
	else:
		form = BlogForm()
	context = {'form': form, }
	return render(request, 'blogs/update.html', context)

def delete(request, id=None):
	if not request.user.is_authenticated:
		raise Http404
	instance = Blog.objects.get(id=id)
	instance.delete()
	messages.add_message(request, messages.ERROR, 'Delete Success.')
	return redirect('blog_home')

