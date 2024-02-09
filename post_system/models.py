from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    name = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete = models.DO_NOTHING, related_name = 'posts')

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete = models.DO_NOTHING, related_name = 'comments')
    post = models.ForeignKey('Post', on_delete = models.DO_NOTHING, related_name = 'comments')

    def __str__(self):
        return self.text
