from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('table/<slug:name>', views.update_table, name='update_table'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/logout/', logout),
]