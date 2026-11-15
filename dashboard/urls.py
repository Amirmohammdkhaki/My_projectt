from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from . import views

app_name = "dashboard"

staff_required = user_passes_test(
    lambda u: u.is_authenticated and u.is_staff,
    login_url="/accounts/login/",
)

urlpatterns = [
    path("", staff_required(views.user_list), name="user_list"),
    path("user/<int:user_id>/plan/", staff_required(views.user_plan), name="user_plan"),
    path("plan/<int:plan_id>/pdf/", views.download_plan_pdf, name="download_pdf"),
    path("plan/<int:plan_id>/send/", staff_required(views.send_plan_email), name="send_plan_email"),  # ⭐
]