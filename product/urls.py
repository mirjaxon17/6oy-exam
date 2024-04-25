from django.urls import path
from .views import HomeListView
from customer.views import UserRegisterView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
]
