from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


# ⭐ ویو «برنامه من» — کاربر عادی
@login_required
def my_plans(request):
    plans = request.user.workout_plans.filter(is_active=True).order_by("-created_at")
    return render(request, "accounts/my_plans.html", {"plans": plans})