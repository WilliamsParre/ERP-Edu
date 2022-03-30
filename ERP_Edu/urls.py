from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/login/admin/', admin.site.urls),

    path('', include('home.urls')),
    path('user/', include('base.urls'))
]
