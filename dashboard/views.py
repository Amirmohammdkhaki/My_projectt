from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from .decorators import staff_required
from .forms import WorkoutPlanForm
from .models import WorkoutPlan

User = get_user_model()


# ==========================
# لیست کاربران
# ==========================

@staff_required
def user_list(request):
    users = User.objects.filter(is_staff=False).order_by("-date_joined")
    return render(request, "dashboard/user_list.html", {"users": users})


# ==========================
# ثبت برنامه برای کاربر
# ==========================

@staff_required
def user_plan(request, user_id):
    target = get_object_or_404(User, id=user_id)
    plans = target.workout_plans.all()

    if request.method == "POST":
        form = WorkoutPlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = target
            plan.created_by = request.user
            plan.save()
            messages.success(request, f"برنامه برای {target.email} ثبت شد.")
            return redirect("dashboard:user_plan", user_id=target.id)
    else:
        form = WorkoutPlanForm()

    return render(request, "dashboard/user_plan.html", {
        "target": target,
        "plans": plans,
        "form": form,
    })


# ==========================
# ⭐ ارسال برنامه به ایمیل کاربر
# ==========================

@staff_required
def send_plan_email(request, plan_id):
    plan = get_object_or_404(WorkoutPlan, id=plan_id)

    if not plan.user.email:
        messages.error(request, "این کاربر ایمیل ندارد.")
        return redirect("dashboard:user_plan", user_id=plan.user.id)

    subject = f"برنامه تمرینی شما — {plan.title}"
    body = (
        f"سلام {plan.user.email},\n\n"
        f"برنامه تمرینی «{plan.title}» برای شما ثبت شد.\n"
        f"تاریخ شروع: {plan.start_date}\n"
    )
    if plan.end_date:
        body += f"تاریخ پایان: {plan.end_date}\n"
    if plan.content:
        body += f"\nتوضیحات:\n{plan.content}\n"
    body += "\nبا آرزوی موفقیت — باشگاه شیران 🦁"

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[plan.user.email],
    )

    # ⭐ اگر PDF دارد، ضمیمه کن
    if plan.pdf_file:
        try:
            plan.pdf_file.open("rb")
            email.attach(
                filename=f"{plan.title}.pdf",
                content=plan.pdf_file.read(),
                mimetype="application/pdf",
            )
            plan.pdf_file.close()
        except Exception as e:
            messages.warning(request, f"PDF ضمیمه نشد: {e}")

    try:
        email.send()
        messages.success(request, f"برنامه به {plan.user.email} ایمیل شد.")
    except Exception as e:
        messages.error(request, f"ارسال ایمیل ناموفق: {e}")

    return redirect("dashboard:user_plan", user_id=plan.user.id)


# ==========================
# دانلود PDF — محافظت‌شده
# ==========================

@login_required
def download_plan_pdf(request, plan_id):
    plan = get_object_or_404(WorkoutPlan, id=plan_id)

    if not (request.user == plan.user or request.user.is_staff):
        raise Http404

    if not plan.pdf_file:
        raise Http404

    return FileResponse(
        plan.pdf_file.open("rb"),
        as_attachment=True,
        filename=f"{plan.title}.pdf",
    )