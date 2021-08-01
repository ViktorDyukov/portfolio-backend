from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AllCasesSerializer, LinkSerializer, CaseDetailSerializer, PageSerializer
from .models import Case, Link, Customisation, Page
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.conf import settings
import logging
logger = logging.getLogger(__file__)


class CaseView(APIView):
    def get(self, request, link):
        logger.error("222")
        try:
            cust_id = Link.objects.get(link_ext=link).customisation.id
        except ObjectDoesNotExist:
            cust_id = settings.PUB_CUSTOMIZATION

        if cust_id == settings.PUB_CUSTOMIZATION:
            queryset = Case.objects.filter(isPublic=True)
        else:
            queryset = Case.objects.all().order_by('order')

        serializer = AllCasesSerializer(queryset, many=True)
        response = Response(serializer.data)
        return response


class CaseDetailView(APIView):
    def get(self, request, id):
        try:
            queryset = Case.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
        serializer = CaseDetailSerializer(queryset)
        response = Response(serializer.data)
        return response


class LinkView(APIView):
    def get(self, request, link):
        queryset = Link.objects.filter(link_ext=link)
        if len(queryset) == 0:
            queryset = Link.objects.filter(link_ext='public')
        serializer = LinkSerializer(queryset[0])
        response = Response(serializer.data)
        return response

class PageView(APIView):
    def get(self, request, purl):
        queryset = Page.objects.get(url=purl)
        template = Template('{% load martortags %}{{ bd | safe_markdown}}')
        context = Context(dict(bd=queryset.body))
        body = template.render(context)
        queryset.body = body
        serializer = PageSerializer(queryset)
        response = Response(serializer.data)
        return response
