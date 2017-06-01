from django.conf.urls import url
from rango import views
urlpatterns = [
url(r'^$', views.index, name='about1'),
url(r'^about/', views.about, name='about1'),
]
