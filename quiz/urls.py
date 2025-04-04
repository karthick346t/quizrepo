from django.urls import path
from .views import home, user_login, user_logout, signup, quiz

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('quiz/', quiz, name='quiz'),
]
