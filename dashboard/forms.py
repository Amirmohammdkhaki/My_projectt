from django import forms
from .models import WorkoutPlan


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ["title", "start_date", "end_date", "content", "pdf_file", "is_active"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "مثلاً برنامه حجم — هفته ۱",
            }),
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "حرکات، ست، تکرار، استراحت...",
            }),
        }

    def clean_pdf_file(self):
        pdf = self.cleaned_data.get("pdf_file")
        if pdf:
            if not pdf.name.lower().endswith(".pdf"):
                raise forms.ValidationError("فقط فایل PDF مجاز است.")
            if pdf.size > 10 * 1024 * 1024:  # 10 MB
                raise forms.ValidationError("حجم فایل نباید بیشتر از ۱۰ مگابایت باشد.")
        return pdf