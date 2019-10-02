from django.conf.urls import url, include
from django.views.generic import TemplateView

from decorator.core import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^comments/$', views.comments, name='comments')
]
