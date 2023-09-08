from django.contrib import admin
from django.urls import include, path
from reg import views as regViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("reg/", regViews.registration, name="registration"),
    path("profile/", regViews.profile, name="profile"),
    path(
        "user/", authViews.LoginView.as_view(template_name="reg/user.html"), name="user"
    ),
    path(
        "exit/",
        authViews.LogoutView.as_view(template_name="reg/exit.html"),
        name="exit",
    ),
]
