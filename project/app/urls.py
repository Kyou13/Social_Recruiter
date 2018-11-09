from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.DashboardPage.as_view(), name='dashboard'),
#     path('user/', views.UserPage.as_view(), name='user'),
    path('tables/', views.TablesPage.as_view(), name='tables'),
#     path('message/create/', views.GetMessage.as_view(), name='create'),
#     path('message/edit/<int:pk>', views.UpdateMessage.as_view(), name='edit'),
#     path('message/delete/<int:pk>', views.DeleteMessage.as_view(), name='delete'),
    path('contact/',views.ContactView.as_view(), name='contact'),
]
