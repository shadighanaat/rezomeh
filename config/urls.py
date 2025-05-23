"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

admin_url = os.environ.get('DJANGO_ADMIN_URL', 'admin') 

urlpatterns = [
    path(f'{admin_url}/', admin.site.urls),
    path('rezomeh/', include('rezomeh.urls')),

    
    # rosseta (i18)
    path('rosetta/', include('rosetta.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
