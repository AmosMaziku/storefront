from django.db import models
from django.contrib.contenttypes.models import ContentTypes 
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    title = models.CharField(max_legnth=255)


class TggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentTypes, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()