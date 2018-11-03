from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')

def education(request):
	return render(request,'personal/education.html')

def projects(request):
	return render(request,'personal/projects.html')

def skills(request):
	return render(request,'personal/skills.html')

def design(request):
	return render(request,'personal/design.html')

def hobby_zone(request):
	return render(request,'personal/hobby_zone.html')