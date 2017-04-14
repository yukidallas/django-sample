from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from . import views


urlpatterns = [
  url(r'^$', views.home_view),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^auth/', include('allauth.urls')),
  url(r'^signin/?$', views.signin_view),
  url(r'^signup/?$', views.signup_view),
  url(r'^signout/?$', views.signout_view)
]
