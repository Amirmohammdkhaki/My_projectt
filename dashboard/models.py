from django.db import models
from django.conf import settings


class WorkoutPlan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workout_plans",
    )
    title = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    content = models.TextField(help_text="حرکات، ست، تکرار، استراحت", blank=True)

    # ⭐ فیلد جدید: فایل PDF
    pdf_file = models.FileField(
        upload_to="workout_pdfs/%Y/%m/",
        blank=True,
        null=True,
        help_text="فایل PDF برنامه (اختیاری)",
    )

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="plans_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} — {self.title}"