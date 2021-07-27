from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("api/cases_test/", views.CaseView.as_view()),
    path("api/highlights/<int:link>/", views.LinkView.as_view()),
    path("api/case/<int:id>/", views.CaseDetailView.as_view()),
    path("api/page/<str:purl>/", views.PageView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)