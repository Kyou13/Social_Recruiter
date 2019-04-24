from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.SigninView.as_view(), name='top'),
  path('home', views.DashBoard.as_view(), name='dashboard'),
  path('logout', views.SignoutView.as_view(), name='signout'),
  path('user_list/<int:page>', views.UserList.as_view(), name='user_list'),
  # path('login', views.SigninView.as_view(), name='signin'),
]
