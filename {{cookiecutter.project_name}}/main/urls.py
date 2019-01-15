from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import {{cookiecutter.model_view_name}}

router = DefaultRouter()

# router.register('sentiment', SentimentAnalysisView, base_name="sentiments")

urlpatterns = [
    url(r'{{cookiecutter.model_name}}', {{cookiecutter.model_view_name}}.as_view()),
]
