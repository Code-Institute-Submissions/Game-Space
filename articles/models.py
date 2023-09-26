from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Article model strutcture
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
