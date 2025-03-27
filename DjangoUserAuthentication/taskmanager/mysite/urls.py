from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("taskmanager.urls")),
    path('admin-panel/', include('taskmanager.admin_urls')),
]
