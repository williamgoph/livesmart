from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/$', views.user, name='user'),
    #url(r'^user/(\w+)/(\d+)/$', views.user, name='user'),
    url(r'^goal/(?P<goal_id>[0-9]+)/$', views.goal, name='goal'),
    url(r'^entries/$', views.entries, name='entries'),
    url(r'^successful/$', views.successful, name='successful'),
    url(r'^delgoal/(?P<goal_id>[0-9]+)/$', views.delgoal, name='delgoal'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]
