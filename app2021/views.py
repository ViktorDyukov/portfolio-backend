from .serializers import AllCasesSerializer, LinkSerializer, CaseDetailSerializer, PageSerializer
from .models import Case, Link, Customisation, Page
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.template import Template, Context
from django.conf import settings
import pdfrw
import io


class CaseView(APIView):
    def get(self, request, link):
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


class CVView(View):
    def get(self, request, link):
        pdf = pdfrw.PdfReader("templates/cv.pdf")
        new_pdf = pdfrw.PdfWriter()
        for page in pdf.pages:
            for annot in page.Annots or []:
                old_url = annot.A.URI.decode()
                if old_url.find('portfolio.victorduco.com') != -1:
                    new_url = old_url.replace('portfolio.victorduco.com', '{}.victorduco.com'.format(link))
                    new_url = pdfrw.objects.pdfstring.PdfString("({})".format(new_url))
                    annot.A.URI = new_url
            new_pdf.addpage(page)
        buf = io.BytesIO()
        new_pdf.write(buf)
        buf.seek(io.SEEK_SET)
        try:
            return FileResponse(buf, content_type='application/pdf', as_attachment=True, filename="Victor Dyukov - CV.pdf")
        except FileNotFoundError:
            raise Http404()
