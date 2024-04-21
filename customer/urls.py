from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
]