from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app import views, auth

app_name = 'records'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name = 'detail'),
    url(r'^$', views.success, name = 'success'),
    url(r'student/addition/$',views.StudentAdd.as_view(), name = 'student-addition'),
    url(r'student/add/$',views.RecordCreate.as_view(), name = 'student-add'),

    url(r'student/(?P<pk>[0-9]+)/$',views.RecordUpdate.as_view(), name = 'student-update'),

    url(r'student/(?P<pk>[0-9]+)/delete/$',views.StudentDelete.as_view(), name = 'student-delete'),

    url(r'^login/', auth.login, name = 'login'),
    url(r'^logout/', auth.logout, name = 'logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
