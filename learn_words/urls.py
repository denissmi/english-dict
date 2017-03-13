from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^english/$', views.EnglishWordList.as_view()),
    url(r'^english/(?P<pk>[0-9]+)/$', views.EnglishWordDetail.as_view()),
    url(r'^russian/$', views.RussianWordList.as_view()),
    url(r'^russian/(?P<pk>[0-9]+)/$', views.RussianWordDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]