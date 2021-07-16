from django.urls import path
from .views import RegisterView, LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='customer-register'),
    path('login/', LoginView.as_view(), name='customer-login'),
    path('logout/', LogoutView.as_view(), name='customer_logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
