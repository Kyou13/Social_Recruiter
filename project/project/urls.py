from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # 認証
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('social_django.urls', namespace='social')),
    # アプリケーション
    path('', include('app.urls')),
]
