from django.urls import include, path
from rest_framework import routers
from . import views


urlpatterns = [
    path("projects/", views.ProjectView.as_view()),
    path("links/<int:link>/", views.LinkView.as_view()),
    path("project/<int:id>/", views.ProjectDetailView.as_view()),
    path("page/<int:id>/", views.PageView.as_view()),



]