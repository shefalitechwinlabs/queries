"""crud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from crud_app.views import profile


urlpatterns = [
    path('home/', include('crud_app.urls')),
    path('profile/', profile ,name='profile'), 
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
handler404 = "crud_app.views.page_not_found_view"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
