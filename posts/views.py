from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .forms import PostForm
from .models import Post


def post_detail(request,slug):
	instance= get_object_or_404(Post,slug=slug)
	context={  
		"title":instance.title,
		"instance":instance,
	}
	return render(request,"posts/post_detail.html",context)

def post_list(request):
	queryset=Post.objects.all()
	context={
		"Object_list":queryset,
		"title":"List"
	}
	return render(request,"posts/post_list.html",context)



