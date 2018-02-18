from django.conf.urls import url

from mysite import settings
from . import views
from django.views.static import serve


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'result', views.result, name='result')
]