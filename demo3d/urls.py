from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls import include
from django.contrib.auth import views as auth_views

from .views import home_view, details


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('<int:pk>', details, name = 'details')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


