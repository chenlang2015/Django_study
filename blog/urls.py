from django.urls import path
from .views import SubjectsView, TeachersView, PolicyView

urlpatterns = [
    path("teachers/", TeachersView.as_view()),
    path("subjects/", SubjectsView.as_view()),
    path("policy/<id>/",PolicyView.as_view()),
]