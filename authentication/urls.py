from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from authentication import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)