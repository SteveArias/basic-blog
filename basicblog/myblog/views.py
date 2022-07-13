from django.shortcuts import render
from .models import BlogPost, BlogAuthor

def index(request):
	"""View function for home page of site."""

	num_blog_posts = BlogPost.objects.all().count()
	num_authors = BlogAuthor.objects.all().count()
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'num_blog_posts': num_blog_posts,
		'num_authors': num_authors,
		'num_visits': num_visits
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)