from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)', views.post, name='post'),
    url(r'^new/post$', views.new_post, name='new-post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)