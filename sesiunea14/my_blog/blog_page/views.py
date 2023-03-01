from django.shortcuts import render, get_object_or_404
from .models import ArticlePost


# Create your views here.
def home(request):
    articles = ArticlePost.objects.all()
    username = request.user.username
    return render(request, 'home.html', {'articles': articles,
                                         'username': username})


def article_details(request, article_id):
    article = get_object_or_404(ArticlePost, pk=article_id)
    return render(request, 'article_details.html', {'article': article})
