from django.urls import path
from account.views import register, login, logout, ProfileUpdateView,forget_password,reset_password

app_name = 'account'
urlpatterns = [
    path('register', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('forget_password/', forget_password, name='forget_password'),
    path('profile-edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path("reset_password/<str:uidb64>/<str:token>/",reset_password,name='reset_password'),

]