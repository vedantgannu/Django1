from django.shortcuts import render
from django.http import HttpResponse#I added

#Sample data
posts = [
	{
		'author': 'VedantG',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2018'
	}
]

# Create your views here.
def home(request):
	#Dictionary representing sample data. We want to get this data into home.html
	context = {
		'posts': posts
	}
	#return HttpResponse('<h1>Blog Home</h1>')
	return render(request, 'blog/home.html', context)
	#Render function loads in the template html file we want to use for this function
	#The template.html file can be accessed through 'blog/home.html'. This means from the
	#templates folder in Blog, access the home.html file that is located in "blog" folder

def about(request):
	#return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html', {'title': 'About'})
#blog->templates->blog->templates.html stuff