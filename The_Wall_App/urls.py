from django.urls import path
from . import views
urlpatterns =[
    path('', views.wallView),
    path('/postMessage', views.postMessage),
    path('/postcomment/<int:id>' , views.postComment),
    path('/deletemessage/<int:id>', views.deletemessage),
]