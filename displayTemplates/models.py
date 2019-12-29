from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=101)
    img = models.ImageField(upload_to='template_icons')
    desc = models.TextField()
    value = models.CharField(max_length=101)
