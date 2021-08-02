from rest_framework import serializers
from .models import Case, Link, Customisation, Tag, Page, CaseImage, CaseInfoSection
from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from django.template import Template, Context
from django.conf import settings


class ThumbnailSerializer(serializers.ImageField):
    def __init__(self, alias, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_only = True
        self.alias = alias

    def to_representation(self, value):
        if not value:
            return None

        url = thumbnail_url(value, self.alias)
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CaseImageSerializer(serializers.ModelSerializer):
    imageX1 = ThumbnailSerializer(alias='caseimg_x1', source='imageX2')
    imageX2 = ThumbnailSerializer(alias='caseimg_x2')
    previewX1 = ThumbnailSerializer(alias='caseimg_preview_x1', source='imageX2')
    previewX2 = ThumbnailSerializer(alias='caseimg_preview_x2', source='imageX2')

    class Meta:
        model = CaseImage
        fields = ('imageX1', 'imageX2', 'previewX1', 'previewX2')


class CaseInfoSerializer(serializers.ModelSerializer):
    body = serializers.SerializerMethodField()

    class Meta:
        model = CaseInfoSection
        fields = ('title', 'body', 'order')

    def get_body(self, obj):
        template = Template('{% load martortags %}{{ bd | safe_markdown}}')
        context = Context(dict(bd=obj.body))
        body = template.render(context)
        return body


class AllCasesSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    preview_deskX1 = ThumbnailSerializer(alias='preview_desk_x1', source='preview_deskX2')
    preview_deskX2 = ThumbnailSerializer(alias='preview_desk_x2')

    class Meta:
        model = Case
        fields = ('id', 'title', 'tag', 'preview_deskX1', 'preview_deskX2', 'preview_svg_deskX2')


class CaseDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    separatorImg_deskX1 = ThumbnailSerializer(alias='separatorImg_desk_x1', source='separatorImg_deskX2')
    separatorImg_deskX2 = ThumbnailSerializer(alias='separatorImg_desk_x2')
    caseImage = CaseImageSerializer(source="caseimage_set", many=True)
    caseInfoSection = CaseInfoSerializer(source="caseinfosection_set", read_only=True, many=True)

    class Meta:
        model = Case
        fields = (
            'title', 'bg_color', 'description','separatorImg_deskX1', 'separatorImg_deskX2', 'tag', 'caseImage', 'caseInfoSection')




class CustomizationSerializer(serializers.ModelSerializer):
    highlight = serializers.SerializerMethodField()

    class Meta:
        model = Customisation
        fields = ('intro_header', 'intro_description', 'highlight')

    def get_highlight(self, obj):
        if obj.id != settings.PUB_CUSTOMIZATION:
            queryset = Case.objects.filter(customisation=obj.id)
        else:
            queryset = Case.objects.filter(customisation=obj.id, isPublic=True)
        serializer = AllCasesSerializer(many=True, read_only=True, instance=queryset)
        return serializer.data

class LinkSerializer(serializers.ModelSerializer):
    customisation = CustomizationSerializer(read_only=True)

    class Meta:
        model = Link
        fields = ('customisation',)


class Pg:
    def __init__(self, title, body):
        self.title = title
        self.body = body


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('title', 'body')
