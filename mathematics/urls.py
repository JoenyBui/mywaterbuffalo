from __future__ import unicode_literals

from django.conf.urls import url

from . import views

app_name = 'mathematics'
urlpatterns = [
    url(r'^mathematics/$', views.MathematicsListView.as_view(), name='mathematics_list'),
]