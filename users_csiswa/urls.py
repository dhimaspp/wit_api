from django.conf.urls import url, include
from rest_framework import routers
from .views import *
from django.urls import path

app_name = 'wit_api'
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('jurusan/<int:pk>/', JurusanViewSets.as_view()),
    path('jurusan/', JurusanListViews.as_view()),
    # path('datacsiswa/(?P<pk>\d+)/$', DataCSiswaListViews.as_view()),
]

# urlpatterns = [
#     url(r'^csiswa/$', CSiswaListViews.as_view()),
#     url(r'^csiswa/(?P<pk>\d+)/$', CSiswaViewSets.as_view()),
#     url(r'^jurusan/$', JurusanListViews.as_view()),
#     url(r'^jurusan/(?P<pk>\d+)/$', JurusanViewSets.as_view()),
#         url(r'^admin/$', AdminListView.as_view()),
# ]
