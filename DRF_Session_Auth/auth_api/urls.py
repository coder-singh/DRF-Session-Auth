from django.urls import path
from auth_api.views import registration_view, login_view

app_name = 'auth_api'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
]