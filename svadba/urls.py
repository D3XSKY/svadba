from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from svadba import views

urlpatterns = [
    url(r'^proizvodi/$', views.ProizvodList.as_view()),
    url(r'^proizvodi/(?P<pk>[0-9]+)/$', views.ProizvodDetail.as_view()),
    url(r'^proizvodi/prikaz/$', views.ProizvodSlikaList.as_view()),
    url(r'^proizvodi/prikaz/(?P<pk>[0-9]+)/$', views.ProizvodSlikaDetail.as_view()),
    url(r'^kategorije/$', views.KategorijaList.as_view()),
    url(r'^kategorije/(?P<pk>[0-9]+)/$', views.KategorijaDetail.as_view()),
    url(r'^slike/$', views.SlikaList.as_view()),
    url(r'^slike/(?P<pk>[0-9]+)/$', views.SlikaDetail.as_view()),
    url(r'^index/$', views.first, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^product/$', views.product, name='product'),
]

urlpatterns = format_suffix_patterns(urlpatterns)