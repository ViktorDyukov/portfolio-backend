from rest_framework import serializers
from .models import Project, Link, Customisation, Page


class AllProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'url')

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'url', 'body')

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('name', 'description', 'url', 'body')


class CustomizationSerializer(serializers.ModelSerializer):
    hightlight = AllProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Customisation
        fields = ('name', 'intro', 'hightlight_header', 'hightlight')


class LinkSerializer(serializers.ModelSerializer):
    customisation = CustomizationSerializer(read_only=True)

    class Meta:
        model = Link
        fields = ('name', 'link_ext', 'customisation')
