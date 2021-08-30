from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('userstatus/', UserStatusView.as_view()),
]