"""neobank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.routers import router
from frontend.sitemaps import StaticViewSitemap
from accounts.accounts_views import create_user_profile_android, update_user_profile_android
sitemaps = {
    'static': StaticViewSitemap
}

handler404 = 'frontend.views.handler404'

urlpatterns = [
    # path('admin1/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('frontend.urls')),
    path('crugapp/', include('crugapp.urls')),
    path('partners/', include('partners.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('admin/', include('accounts.accounts_urls')),
    path('cms/',include('accounts.urls')),
    path('neoadmin/', include('accounts.neoadmin_urls')),
    path('api/v1/', include(router.urls)),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/api/createuser/', create_user_profile_android, name='create_user_profile_android'),
    path('accounts/api/updateuser/<int:id>/', update_user_profile_android, name='update_user_profile_android'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
