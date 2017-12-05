from django.conf.urls import url
from django.contrib import admin

from .views import (
	PetCreateAPIView,
    PetDetailAPIView,
    PetDeleteAPIView,
    PetListAPIView,
    PetUpdateAPIView
	)

urlpatterns = [
    url(r'^$', PetListAPIView.as_view(), name='list' ),
    url(r'^create/$', PetCreateAPIView.as_view(), name='create' ),
    url(r'^(?P<pk>\d+)/$', PetDetailAPIView.as_view(), name='detail' ),
    url(r'^(?P<pk>\d+)/edit/$', PetUpdateAPIView.as_view(), name='update' ),
    url(r'^(?P<pk>\d+)/delete/$', PetDeleteAPIView.as_view(), name='delete' )
]