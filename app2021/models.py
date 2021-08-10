from django.db import models
from martor.models import MartorField
import random
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def random_string():
    return str(random.randint(100, 999))


# validators


def prevImage_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width != 2668 or image_height != 1226:
        raise ValidationError('Image width needs to be 2668x1226')

def separatorImage_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width != 2400 or image_height != 1500:
        raise ValidationError('Image width needs to be 2400x1500')

def caseImage_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width != 2576 or image_height != 1600:
        raise ValidationError('Image width needs to be 2576x1600')


# models


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Case(models.Model):
    title = models.CharField(max_length=90)
    tag = models.ManyToManyField(Tag)
    bg_color = models.CharField(max_length=7, default='#666666')
    description = models.TextField(max_length=800, default="")
    isPublic = models.BooleanField(default=True)
    preview_deskX2 = models.ImageField(
        default="",
        validators=[prevImage_restriction],
        upload_to='preview/'
    )
    preview_bgposition = models.CharField(max_length=7, default='50%')
    preview_svg_deskX2 = models.FileField(
        default="",
        upload_to='preview_svg/'
    )

    separatorImg_deskX2 = models.ImageField(
        default="",
        # validators=[separatorImage_restriction],
        upload_to='separatorImg/'
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return "%s" % (self.title)

class CaseInfoSection(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    body = MartorField(null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']


class CaseImage(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    imageX2 = models.ImageField(
        default="",
        validators=[caseImage_restriction],
        upload_to='cases/'
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']


class Customisation(models.Model):
    name = models.CharField(max_length=40)
    intro_header = models.TextField(max_length=100, default='')
    intro_description = models.TextField(max_length=300, default='')
    highlight = models.ManyToManyField(Case)

    def __str__(self):
        return "%s" % (self.name)


class Link(models.Model):
    name = models.CharField(max_length=40)
    link_ext = models.CharField(default=random_string, max_length=20)
    opened = models.IntegerField()
    customisation = models.ForeignKey(Customisation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.link_ext)


class Page(models.Model):
    title = models.TextField(max_length=100, default='')
    body = MartorField(null=True)
    url = models.CharField(max_length=25, default='', unique=True)

    def __str__(self):
        return "%s" % (self.title)