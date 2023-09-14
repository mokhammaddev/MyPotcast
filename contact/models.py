from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=222, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
