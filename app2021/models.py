from django.db import models
from django.db.models.fields.files import ImageField
from martor.models import MartorField
import random
from django.contrib import admin


def random_string():
    return str(random.randint(100, 999))


# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Project(models.Model):
    name  = models.CharField(max_length=40)
    description  = models.CharField(max_length=90)
    url = models.CharField(max_length=30)
    #image_preview = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    body = MartorField()
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return "%s %s" % (self.name, self.url)


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


class Customisation(models.Model):
    name = models.CharField(max_length=15)
    link_ext = models.CharField(max_length=10)
    intro = models.CharField(max_length=220)
    hightlight = models.ManyToManyField(Project)
    hightlight_header = models.CharField(max_length=15)


    def __str__(self):
        return "%s %s" % (self.name, self.link_ext)


class Link(models.Model):
    name = models.CharField(max_length=15)
    link_ext = models.CharField(default = random_string, max_length=3)
    opened = models.IntegerField()
    customisation = models.ForeignKey(Customisation, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return "%s %s" % (self.name, self.link_ext)



class Page(models.Model):
    name  = models.CharField(max_length=30)
    description  = models.CharField(max_length=50)
    url = models.CharField(max_length=30)
    #image_preview = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    body = MartorField()

    def __str__(self):
        return "%s %s" % (self.name, self.url)

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )