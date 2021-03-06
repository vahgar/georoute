from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import index_page, login, logout
from accounts.api.api_views import UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView
urlpatterns = [
    url(r'^index/', index_page, name="index"),
    url(r'^login/',  login, name="login" ),
    url(r'^logout/',  logout, name="logout" ),
    url(r'^user/create$', UserCreateAPIView.as_view(), name='user_create'),
    url(r'^user/api_list$', UserListAPIView.as_view(), name='student_list'),
    url(r'^user/api_list/(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name='user_detail'),
    url(r'^user/api_list/(?P<pk>\d+)/edit$', UserUpdateAPIView.as_view(), name='user_update'),
    url(r'^user/api_list/(?P<pk>\d+)/delete$', UserDeleteAPIView.as_view(), name='user_delete'),
]
