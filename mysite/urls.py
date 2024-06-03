from django.contrib import admin
from django.urls import path

import views


urlpatterns = [
    path("", views.home, name="home"),
    path("sucess/", views.success, name="success"),
    path("admin/", admin.site.urls),
]
