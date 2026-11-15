from django.urls import path
from .views import SignupView, my_plans

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("my-plans/", my_plans, name="my_plans"),   # ⭐ اضافه شد
]