from django.conf.urls import include,url
from rest_framework_jwt.views import obtain_jwt_token

from location.api.api_views import LocationCreateAPIView, LocationListAPIView, LocationDetailAPIView, LocationDeleteAPIView, LocationUpdateAPIView

urlpatterns = [
    url(r'^create$', LocationCreateAPIView.as_view(), name='location_create'),
    url(r'^api_list$', LocationListAPIView.as_view(), name='location_list'),
    url(r'^api_list/(?P<pk>\d+)/$', LocationDetailAPIView.as_view(), name='location_detail'),
    url(r'^api_list/(?P<pk>\d+)/edit$', LocationUpdateAPIView.as_view(), name='location_update'),
    url(r'^api_list/(?P<pk>\d+)/delete$', LocationDeleteAPIView.as_view(), name='location_delete'),
]
