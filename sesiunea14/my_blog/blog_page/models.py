from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_TYPE = [
    ('food', 'Food'),
    ('travel', 'Travel'),
    ('coding', 'Coding')
]


class ArticlePost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_TYPE, null=False)
    image_url = models.CharField(max_length=2083,
                                 default='https://www.farmgirlmarketingsolutions.com/wp-content/uploads/2015/12/blog-pic-b2c.jpg')

    def __str__(self):
        return f'{self.title} | {self.author}'
