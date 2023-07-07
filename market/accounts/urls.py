from django.urls import path

from .views import (
    SignUpView,
    UserLogoutView,
    AuthView,
    ProfileDetailsView,
    AvatarUpdateView,
    PasswordChangeView
)

app_name = "accounts"

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-in'),
    path('sign-out/', UserLogoutView.as_view(), name='sign-out'),
    path('sign-in/', AuthView.as_view(), name='login'),
    path('profile/', ProfileDetailsView.as_view(), name='profile_details'),
    path('profile/avatar/', AvatarUpdateView.as_view(), name='avatar'),
    path('profile/password/', PasswordChangeView.as_view(), name='password'),
]
