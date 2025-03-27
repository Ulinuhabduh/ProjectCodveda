# admin_urls.py
from django.urls import path
from .admin_views import admin_dashboard, delete_user, edit_user
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', staff_member_required(admin_dashboard), name='admin_dashboard'),
    path('delete_user/<int:user_id>/', staff_member_required(delete_user), name='delete_user'),
    path('edit_user/<int:user_id>/', staff_member_required(edit_user), name='edit_user'),
]
