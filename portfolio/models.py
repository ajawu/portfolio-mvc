from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email_address = models.EmailField(blank=False)
    message = models.TextField(blank=False)
