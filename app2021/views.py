from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AllProjectSerializer, LinkSerializer, ProjectDetailSerializer, PageSerializer
from .models import Project, Link, Page
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404


class ProjectView(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        serializer = AllProjectSerializer(queryset, many=True)
        response =  Response(serializer.data)
        return response

class ProjectDetailView(APIView):
    def get(self, request, id):
        try:
            queryset = Project.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
        serializer = ProjectDetailSerializer(queryset)
        response =  Response(serializer.data)
        return response

class PageView(APIView):
    def get(self, request, id):
        queryset = Page.objects.get(id=id)
        serializer = PageSerializer(queryset)
        response =  Response(serializer.data)
        return response

class LinkView(APIView):
    def get(self, request, link):
        queryset = Link.objects.get(link_ext=link)
        serializer = LinkSerializer(queryset)
        response =  Response(serializer.data)
        return response


