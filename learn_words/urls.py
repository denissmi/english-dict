from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^english/$', views.EnglishWordList.as_view()),
    url(r'^english/(?P<pk>[0-9]+)/$', views.EnglishWordDetail.as_view()),
    url(r'^russian/$', views.RussianWordList.as_view()),
    url(r'^russian/(?P<pk>[0-9]+)/$', views.RussianWordDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)