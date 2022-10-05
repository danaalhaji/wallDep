from django.urls import path
from . import views
urlpatterns =[
    path('', views.homePage),
    path('login',views.Login),
    path('signup', views.SignUp),
    path('WelcomNewUser', views.signUpSucess),
    path('welcomUser', views.loginSuccess),
        path('logOut', views.logOutt),
]