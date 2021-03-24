from django.conf.urls import url, include
from rest_framework import routers
from .views import *
from django.urls import path

app_name = 'wit_api'
urlpatterns = [
    path('usercsiswa/', UserCsiswaView.as_view(), name='usercsiswa'),
    path('admin/', AdminView.as_view(), name='admin')
]

# urlpatterns = [
#     url(r'^csiswa/$', CSiswaListViews.as_view()),
#     url(r'^csiswa/(?P<pk>\d+)/$', CSiswaViewSets.as_view()),
#     url(r'^jurusan/$', JurusanListViews.as_view()),
#     url(r'^jurusan/(?P<pk>\d+)/$', JurusanViewSets.as_view()),
#         url(r'^admin/$', AdminListView.as_view()),
# ]
