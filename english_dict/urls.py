from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('learn_words.urls')),
]