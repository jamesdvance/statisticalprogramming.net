from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
]