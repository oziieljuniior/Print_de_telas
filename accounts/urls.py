from django.urls import path
from .views import dashboard, register, ProfileListView, ProfileView, my_view
from django.conf.urls import include

app_name = "System_Post"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile/", ProfileListView.as_view(), name="profile_list"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("my-url/", my_view, name = "my_url")
]