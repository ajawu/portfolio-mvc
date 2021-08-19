from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)


class Project(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.CharField(max_length=300, blank=False)
    goal = models.CharField(max_length=150, blank=False)
    image = models.ImageField(upload_to='projects')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
