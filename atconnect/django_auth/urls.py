from django.contrib import admin
from django.urls import path, include
from atconnect.views import DashboardView
from django.contrib.auth import views


urlpatterns = [
    path("", DashboardView.as_view(), name = "dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls', namespace='accounts')),
    path('atconnect/', include('atconnect.urls', namespace='atconnect')),
    path('logout/', views.LogoutView.as_view(), name="logout"), 
]
