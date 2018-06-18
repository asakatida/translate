from django.urls import path
from django.views.generic import TemplateView
from .views import translation_view


urlpatterns = [
    path('', TemplateView.as_view(template_name="translate.html"), name='translate'),
    path('translation/', translation_view, name='artmap'),
]