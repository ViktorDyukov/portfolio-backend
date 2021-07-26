from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("cases/", views.CaseView.as_view()),
    path("highlights/<int:link>/", views.LinkView.as_view()),
    path("case/<int:id>/", views.CaseDetailView.as_view()),
    path("page/<str:purl>/", views.PageView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)