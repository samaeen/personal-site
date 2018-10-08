from django.shortcuts import render

def index(request):
	return render(request,'home.html')

def education(request):
	return render(request,'education.html')

def projects(request):
	return render(request,'projects.html')

def skills(request):
	return render(request,'skills.html')

def design(request):
	return render(request,'design.html')

def hobby_zone(request):
	return render(request,'hobby_zone.html')