from django.conf.urls import url
from laymeiuser import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='laymeibigmsg/bigmsghome.html'), name='post_list'),
]