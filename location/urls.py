from django.conf.urls import include,url
from rest_framework_jwt.views import obtain_jwt_token

from location.api.api_views import LocationCreateAPIView

urlpatterns = [
    url(r'^create$', LocationCreateAPIView.as_view(), name='location_create'),
]
