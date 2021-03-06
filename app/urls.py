"""presences URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^see/(.*)$', views.see, name='see'),
    url(r'^givemail/$', views.register_email, name='register-email'),
    url(r'^create/$', views.create_session_today, name='create-session-today'),
    url(r'^mail/(.*)$', views.mail, name='feuille'),
    url(r'^feuille/$', views.feuille, name='feuille'),
    url(r'^mailing/$', views.mailing_list, name='mailing'),
    url(r'^(\d\d\d\d-\d\d.*|)$', views.presence, name='presence'),
]
