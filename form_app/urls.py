from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.sel_index,name='sel_index'),
    url(r'fill/france/(?P<access_id>[a-zA-Z0-9]+)/$',views.french_form,name='france_index'),
    url(r'fill/(?P<access_id>[a-zA-Z0-9]+)/$',views.index,name='index'),
    url(r'^(?P<request_id>[0-9]+)/$',views.success,name='success')
]