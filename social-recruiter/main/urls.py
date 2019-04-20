from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.Top.as_view(), name='home'),
  path('home', views.Home.as_view(), name='home'),
  path('logout', views.SignoutView.as_view(), name='signout')
]
