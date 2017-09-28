from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from blog.models import Category, Blog, Topic

# Create your views here.
def blog_display(request, cat_num, post_num):

	current_blog = Blog.objects.get(category_id=int(cat_num), post_num=int(post_num))
	blog_list = Blog.objects.filter(category_id=int(cat_num))

	context ={
		'blog': current_blog,
		'blog_list': blog_list,
	}

	return render(request, 'blog_display.html', context)