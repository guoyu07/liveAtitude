from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Article
from django.http import Http404
# Create your views here.

def home(request):
    post_list = Article.objects.all()
    html = '<p>hello world</p>'
    return render_to_response('home.html', {"post_list": post_list})
    # return HttpResponse(html)


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('post.html', locals())