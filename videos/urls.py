
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListVideosView.as_view(), name='all'),

    url(r'^all/$', views.ListVideosView.as_view(), name='index'),
]

