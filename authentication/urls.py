from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from authentication import views


urlpatterns = [
    path('', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
