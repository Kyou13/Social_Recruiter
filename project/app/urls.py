from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.DashboardPage.as_view(), name='dashboard'),
    path('tables/', views.TablesPage.as_view(), name='tables'),
    path('favorites/', views.FavoritePage.as_view(), name='favorite'),
    path('contact/',views.ContactView.as_view(), name='contact'),
]
