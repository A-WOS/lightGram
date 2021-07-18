from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import singup

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signup/', singup, name='signup'),
]
