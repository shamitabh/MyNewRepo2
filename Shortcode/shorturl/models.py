from django.db import models
from .utils import unique_shortcode_generator
from django.db.models.signals import pre_save


class Shortcode(models.Model):
    """db model for storing url and its short hand code"""
    url = models.CharField(max_length=300)
    shortcode = models.CharField(
        max_length=6, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    lastRedirect = models.DateTimeField(auto_now=True)
    redirectCount = models.IntegerField(default=0)

    def __str__(self):
        return self.shortcode


def assign_shortcode(sender, instance, *args, **kwargs):
    """assign shortcode to an instance if it is blank"""
    if not instance.shortcode:
        instance.shortcode = unique_shortcode_generator(instance)


# this will link the code generator method to the Model before saving any object
pre_save.connect(assign_shortcode, sender=Shortcode)
