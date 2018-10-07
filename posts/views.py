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
	return render(request,"post_detail.html",context)

def post_list(request):
	queryset=Post.objects.all()
	context={
		"Object_list":queryset,
		"title":"List"
	}
	return render(request,"post_list.html",context)


def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'list.html', {'contacts': contacts})
