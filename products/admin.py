from django.contrib import admin
from django import forms
from .models import Category, Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "price": forms.NumberInput(
                attrs={"style": "width:250px;"}
            ),
            "discount_price": forms.NumberInput(
                attrs={"style": "width:250px;"}
            ),
        }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = (
        "title",
        "category",
        "price",
        "discount_price",
        "stock",
        "active",
        "datetime_create",
    )

    list_filter = ("category", "active")

    search_fields = (
        "title",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)