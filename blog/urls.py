from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list,name = 'post_list'), ## 'name' indicates the name of the URL to identify the view
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
]
