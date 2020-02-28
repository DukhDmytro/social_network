from django.db import models


class Messages(models.Model):
    message = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.message} by {self.author}'
