# urls.py
from django.urls import path
from . import views, admin_views
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main, name='main'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

    # Password Reset URLs (Custom)
    path("password_reset/", views.custom_password_reset_view, name="password_reset"),
    path("password_reset/done/", lambda request: render(request, "auth/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.custom_password_reset_confirm_view, name="password_reset_confirm"),
    path("reset/done/", lambda request: render(request, "auth/password_reset_complete.html"), name="password_reset_complete"),
    path('admin-panel/', views.admin_dashboard, name='admin-dashboard'),
    path('admin-panel/edit-user/<int:user_id>/', admin_views.edit_user, name='edit_user'),
    path('admin-panel/delete-user/<int:user_id>/', admin_views.delete_user, name='delete_user'),    
]