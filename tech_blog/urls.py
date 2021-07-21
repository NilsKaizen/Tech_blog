"""tech_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog import urls as b_urls
from users import urls as u_urls
from django.conf.urls.static import static
from tech_blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(b_urls)),
    path('users/', include(u_urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)