"""singularity URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.contrib import admin
from singularity import settings
from rainbow import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^fluff/$', views.fluff, name='fluff'),
    url(r'^fluff/(?P<postId>\d{1,5})/edit$', views.edit, name='edit'),
    url(r'^fluff/(?P<postId>\d{1,5})/(?P<slug>[-\w\d]+)?$', views.post, name='post'),
    url(r'^fluff/(?P<postId>\d{1,5})-(?P<slug>[-\w\d]+)?$', views.post, name='post'),
    url(r'^boing/$', views.dashboard, name='boing'),
    url(r'^concoct/$', views.concoct, name='concoct'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^andgodsaidlettherebelight/$', views.new, name='new'),
]

if settings.DEBUG is True:
    urlpatterns += staticfiles_urlpatterns()
