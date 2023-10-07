from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    allposts=Post.objects.all()
    data_dictionary={}
    for post in allposts:
        data_dictionary[post.title]= post.text
    print(data_dictionary)    

    return render(request, 'blog/post_list.html',{"posts": data_dictionary} )