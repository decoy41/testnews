from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^news', views.get_news),
   url(r'^new', views.post_new),
   url(r'^login', views.login),
]