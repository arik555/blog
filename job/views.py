from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib import messages, auth
from .models import *
from .forms import *
# Create your views here.
def home(request):
	jobs = Job.objects.all()
	context = {'jobs': jobs, }
	return render(request, 'jobs/index.html', context)

def update(request, id=None):
	if not request.user.is_authenticated:
		raise Http404
	instance = Job.objects.get(id=id)
	if request.method == 'POST':
		form = JobForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Update Success.')
			return redirect('job_home')
	else:
		form = JobForm(instance=instance)
	context = { 'form': form, 'head': 'EDIT RECORD'}
	return render(request, 'jobs/update.html', context)

def add(request):
	if not request.user.is_authenticated:
		raise Http404
	if request.method == 'POST':
		form = JobForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.add_message(request, messages.SUCCESS, 'Add Success.')
			return redirect('job_home')
	else:
		form = JobForm()
	context = {'form': form, 'head': 'ADD INTO DATABASE'}
	return render(request, 'jobs/update.html', context)

def delete(request, id=None):
	if not request.user.is_authenticated:
		raise Http404
	instance = Job.objects.get(id=id)
	instance.delete()
	messages.add_message(request, messages.ERROR, 'Delete Success.')
	return redirect('job_home')

#########################################################
def add_my_user(request):
	if request.user.is_authenticated:
		return HttpResponse('<h2>Logout and try again.</h2>')
	if request.method == 'POST':
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			ins_obj = form.save(commit=False)
			ins_obj.save()
			messages.success(request, 'Register Success.')
			return redirect('user_login')
	else:
		form = UserRegisterForm()
	context = {'form': form, 'title': 'SignUp',}
	return render(request, 'users/register.html', context)

def login_my_user(request):
	if request.user.is_authenticated:
		return HttpResponse('<h2>Already Logged In.</h2>')
	if request.method == 'POST':
		form = UserLoginForm(request.POST or None)
		if form.is_valid():
			user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				auth.login(request, user)
				messages.success(request, 'Login Success.')
				return redirect('job_home')
			else:
				return HttpResponse('User does not exist!')
	else:
		form = UserLoginForm()
	context = {'form': form, 'title': 'Login',}
	return render(request, 'users/login.html', context)

def update_my_user(request):
	if not request.user.is_authenticated:
		raise Http404
	if request.method == 'POST':
		form = UserEditForm(request.POST or None, instance=request.user)
		if form.is_valid():
			ins_obj = form.save(commit=False)
			ins_obj.save()
			messages.success(request, 'Profile Updated.')
			return redirect('user_details')
	else:
		form = UserEditForm(instance=request.user)
	context = {'form': form, 'title': 'Update Profile', 'flag': '1',}
	return render(request, 'users/register.html', context)

def logout_my_user(request):
	if not request.user.is_authenticated:
		raise Http404
	if request.user.is_authenticated:
		auth.logout(request)
		messages.success(request, "Logout Success.")
		return redirect('user_login')
	else:
		return HttpResponse('Login first.')

def display_profile(request):
	if not request.user.is_authenticated:
		raise Http404
	instance = request.user
	context = {'instance': instance, 'title': 'My Profile', }
	return render(request, 'users/myprofile.html', context)