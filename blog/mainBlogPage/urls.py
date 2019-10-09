from django.contrib import admin
from django.urls import path
from django.urls.static import static
from . import views
from ...blog import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
