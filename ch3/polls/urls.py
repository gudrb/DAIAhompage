from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<choice_id>\d+)/okay/$',views.okay,name='okay'),
    url(r'^(?P<member_id>\d+)/detail/$',views.detail,name='detail'),
    url(r'^(?P<member_id>\d+)/modify/$',views.modify,name='modify'),
]