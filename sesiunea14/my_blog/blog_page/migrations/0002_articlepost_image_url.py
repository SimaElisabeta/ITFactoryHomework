# Generated by Django 4.1.7 on 2023-02-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='image_url',
            field=models.CharField(default='https://www.farmgirlmarketingsolutions.com/wp-content/uploads/2015/12/blog-pic-b2c.jpg', max_length=2083),
        ),
    ]