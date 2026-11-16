from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from core import views
from experiencias import views as experiencias_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='core/login.html'
        ),
        name='login'
    ),

    path(
        'inscribirse/<int:experiencia_id>/',
        experiencias_views.inscribirse,
        name='inscribirse'
    ),
]