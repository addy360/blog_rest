from django.db import models

# Create your models here.


class BlogPics(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField('blog')

    def __str__(self):
        return self.image.url


class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    images = models.ManyToManyField(BlogPics)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title



