from django.urls import path
from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^article/',views.ArticleList.as_view()),
    url(r'^voters/(?P<pk>[0-9]+)/$',views.VoterListDetails.as_view()),
    url(r'^voters/(?P<name>\W+)/$',views.VoterSearch.as_view()),
    url(r'^voters/',views.VoterList.as_view()),
    url(r'^pollinfo/',views.PolledInfoList.as_view()),
	path('', views.index, name='index'),
]