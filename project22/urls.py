from app22.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib import admin



urlpatterns = [
    path("receipepage/",receipes),
    path("loginpage/",login_page),
    path("logoutpage/",logout_page),
    path("registerpage/",register),
    path("deletereceipe/<id>/",delete_receipe,name="delete receipe"),
    path("updatereceipe/<id>/",update_receipe,name="update receipe"),
    path("admin/",admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()