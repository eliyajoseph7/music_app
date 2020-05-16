from django.db import models
from django.utils.text import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Author(models.Model):
    first_name  = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email = models.EmailField()
    # date  = models.DateField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    


class Post(models.Model):
    title           = models.CharField(max_length=50, blank=True, null=True)
    description     = models.TextField(max_length=500)
    body            = models.TextField(default='', blank=True)
    video_url       = models.URLField(max_length=500)
    slug            = models.SlugField(default='', blank=True, max_length=40, unique=True)
    image           = models.ImageField(upload_to='post_images')
    info_source     = models.CharField(max_length=100, blank=True)
    date            = models.DateField(auto_now=True)
    author          = models.ForeignKey(Author, on_delete=models.CASCADE)
    # author_id       = models.IntegerField()
    image_thumbnail = ImageSpecField(source='image',
                                        processors=[ResizeToFill(1332, 850)],
                                        format='JPEG',
                                        options={'quality': 70})

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title
        