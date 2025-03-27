# admin_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .models import Task
from django.contrib import messages
from .form import CustomUserChangeForm

# Cek apakah user adalah staff/admin
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = User.objects.count()
    total_tasks = Task.objects.count()
    return render(request, "admin/admin_dashboard.html", {
        "total_users": total_users,
        "total_tasks": total_tasks,
    })

@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect("admin_dashboard")

@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, "admin_panel/edit_user.html", {"form": form, "user": user})
