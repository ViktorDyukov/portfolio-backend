from rest_framework import serializers
from .models import Case, Link, Customisation, Tag, Page, CaseImage
from easy_thumbnails.templatetags.thumbnail import thumbnail_url


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
        fields = ('id','name')

class CaseImageSerializer(serializers.ModelSerializer):
    imageX1 = ThumbnailSerializer(alias='caseimg_x1', source='imageX2')
    imageX2 = ThumbnailSerializer(alias='caseimg_x2')
    previewX1 = ThumbnailSerializer(alias='caseimg_preview_x1', source='imageX2')
    previewX2 = ThumbnailSerializer(alias='caseimg_preview_x2', source='imageX2')

    class Meta:
        model = CaseImage
        fields = ('imageX1', 'imageX2', 'previewX1', 'previewX2')


class AllCasesSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    preview_deskX1 = ThumbnailSerializer(alias='preview_desk_x1', source='preview_deskX2')
    preview_deskX2 = ThumbnailSerializer(alias='preview_desk_x2')

    class Meta:
        model = Case
        fields = ('id', 'title', 'tag', 'preview_deskX1', 'preview_deskX2')


class CaseDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    caseImage = CaseImageSerializer(source="caseimage_set", many=True)

    class Meta:
        model = Case
        fields = (
        'title', 'bg_color', 'date', 'tag', 'c1_title', 'c1_body', 'c2_title', 'c2_body', 'c3_title', 'c3_body',
        'c4_title', 'c4_body', 'caseImage')


class CustomizationSerializer(serializers.ModelSerializer):
    highlight = AllCasesSerializer(many=True, read_only=True)

    class Meta:
        model = Customisation
        fields = ('intro_header', 'intro_description', 'highlight')


class LinkSerializer(serializers.ModelSerializer):
    customisation = CustomizationSerializer(read_only=True)

    class Meta:
        model = Link
        fields = ('customisation',)


class Pg:
    def __init__(self, title, body):
        self.title = title
        self.body = body


# class PageSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     body = serializers.CharField()


class PageSerializer(serializers.ModelSerializer):
    # test = Template('{% load markdownify %}{{body | markdownify}}')
    # print(test)
    class Meta:
        model = Page
        fields = ('title', 'body')
