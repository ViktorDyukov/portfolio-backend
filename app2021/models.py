from django.db import models
from martor.models import MartorField
import random
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_save
from easy_thumbnails.files import get_thumbnailer
import subprocess
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases


# image optimisation signals


saved_file.connect(generate_aliases)


def optimizePreviewImg(sender, instance, **kwargs):
    # thumb_url = get_thumbnailer(instance.preview_deskX2)['preview_desk_x2'].url
    # thumb_url = get_thumbnailer(instance.preview_deskX2)['preview_desk_x1'].url
    # thumb_url = get_thumbnailer(instance.separatorImg_deskX2)['separatorImg_desk_x1'].url
    # thumb_url = get_thumbnailer(instance.separatorImg_deskX2)['separatorImg_desk_x2'].url
    svg_path = instance.preview_svg_deskX2.path
    batcmd = ["svgo", svg_path, "-o", svg_path]
    r = subprocess.call(batcmd)


# def optimizeCaseImg(sender, instance, **kwargs):
#     thumb_url = get_thumbnailer(instance.imageX2)['caseimg_x1'].url
#     thumb_url = get_thumbnailer(instance.imageX2)['caseimg_x2'].url
#     thumb_url = get_thumbnailer(instance.imageX2)['caseimg_preview_x1'].url
#     thumb_url = get_thumbnailer(instance.imageX2)['caseimg_preview_x2'].url


# validators

def validate_svg(file):
    if file.name[-4:] != ".svg":
        raise ValidationError('The file is not SVG')



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


# Random stuff

def random_string():
    return str(random.randint(100, 999))


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
    slidesLink = models.URLField(
        max_length=128,
        blank=True
    )
    preview_deskX2 = ThumbnailerImageField(
        default="",
        validators=[prevImage_restriction],
        upload_to='preview/'
    )
    preview_bgposition = models.CharField(max_length=7, default='50')
    preview_svg_deskX2 = models.FileField(
        default="",
        upload_to='preview_svg/',
        validators=[validate_svg]
    )

    separatorImg_deskX2 = ThumbnailerImageField(
        default="",
        # validators=[separatorImage_restriction],
        upload_to='separatorImg/'
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return "%s" % (self.title)


post_save.connect(optimizePreviewImg, sender=Case)


class CaseInfoSection(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    body = MartorField(null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']


class CaseImage(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    imageX2 = ThumbnailerImageField(
        default="",
        validators=[caseImage_restriction],
        upload_to='cases/'
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']


# post_save.connect(optimizeCaseImg, sender=CaseImage)


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