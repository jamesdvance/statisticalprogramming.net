from django.shortcuts import render, redirect

# Create your views here.

def about(request):
	return render(request, 'about.html')

def home(request):
	return redirect('/videos/01/01')
