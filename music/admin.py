from django.contrib import admin
from .models import Post, Author, InfoSource, WordsOfWisdom

# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(InfoSource)
admin.site.register(WordsOfWisdom)