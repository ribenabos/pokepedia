from django.urls import path

from . import views
from .views import signup, signup_success

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/success/', signup_success, name='signup_success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
