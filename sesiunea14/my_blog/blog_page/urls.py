from django.urls import path
from . import views

app_name = 'blog_page'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_details, name='article_details')
]
