from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        include("pages.urls")
    ),

    path(
        "accounts/",
        include("allauth.urls")
    ),

]


# ==========================
# Media Files
# نمایش عکس محصولات و کاربران
# فقط در حالت Debug
# ==========================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )