# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .form import CustomUserCreationForm, LoginForm, TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required, user_passes_test


from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from .form import CustomPasswordResetForm, CustomUserChangeForm
from django.urls import reverse
from django.contrib.auth.forms import SetPasswordForm
from django.utils.timezone import now


User = get_user_model()

def custom_password_reset_view(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = request.build_absolute_uri(reverse("password_reset_confirm", kwargs={
                    "uidb64": uid,
                    "token": token
                }))

                email_subject = "🔐 Password Reset Request"
                email_body_plain = f"Hello {user.username},\n\nClick the link below to reset your password:\n{reset_url}\n\nIf you didn't request this, ignore this email.\n\n- TaskMaster Team"

                email_body_html = render_to_string("auth/password_reset_email.html", {
                    "user": user,
                    "reset_url": reset_url
                })

                send_mail(
                    email_subject,
                    email_body_plain,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    html_message=email_body_html  # 🔥 Ini yang bikin email bisa dikirim dalam format HTML!
                )

                messages.success(request, "A password reset email has been sent.")
                return redirect("password_reset_done")

            except User.DoesNotExist:
                messages.error(request, "No user found with this email.")
    
    else:
        form = CustomPasswordResetForm()
    
    return render(request, "auth/password_reset.html", {"form": form})


def custom_password_reset_confirm_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been reset successfully.")
                return redirect("password_reset_complete")
        else:
            form = SetPasswordForm(user)
        return render(request, "auth/password_reset_confirm.html", {"form": form})
    else:
        messages.error(request, "Invalid or expired reset link.")
        return redirect("password_reset")

def home(request):
    return render(request, 'home.html')

# Registrasi User
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_superuser:
                    return redirect('admin_dashboard')
                return redirect('main')
            else:
                messages.error(request, "Invalid username or password") 
        else:
            messages.warning(request, "Form is invalid. Please check your input.") 
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Logout User
def logout_view(request):
    logout(request)
    return redirect('login')

# Halaman Main (Dashboard)
@login_required
def main(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm(request.POST or None)
    if form.is_valid():
        # messages.success(request, "Login successfully.")
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('main')
    
    return render(request, 'main.html', {'tasks': tasks, 'form': form})

# Edit Task
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

# Hapus Task
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('main')
    return render(request, 'delete_task.html', {'task': task})

# Cek apakah user adalah admin
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    return render(request, 'admin_panel/dashboard.html', {'users': users, 'tasks': tasks})

@login_required
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_panel/manage_users.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def manage_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'admin_panel/manage_tasks.html', {'tasks': tasks})

