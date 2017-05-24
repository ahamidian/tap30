from django.conf.urls import include, url
from django.contrib import admin
from core import views
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^send_location$', views.send_location),
    url(r'^get_location$', views.get_location),
    url(r'^admin/', include(admin.site.urls)),
]
