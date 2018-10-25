from django.conf.urls import url
from classbase import views

app_name='classbase'
urlpatterns=[
    url(r'^$',views.SchoolView.as_view(),name='SchoolView'),
    url(r'^(?P<pk>\d+)/$',views.StudentView.as_view(),name='StudentView'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),



]