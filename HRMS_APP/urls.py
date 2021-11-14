"""HRMS_APP URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.generic import TemplateView
from .import views

app_name = 'userHome'

urlpatterns = [
    path('aaaastark/', admin.site.urls),
    path('',views.index_view,name='home'),
    # path('',TemplateView.as_view(template_name="index_main.html")),
    path('user_login/',views.user_login,name='user_login'),
    path('user_register/',views.user_register,name='user_register'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('employees/',include(('Employee.urls','Employee'),namespace='Employee')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

admin.site.site_header = "AAAA STARK (HRMS)"
admin.site.site_title = "AAAA STARK (HRMS)"
admin.site.index_title = "AAAA STARK (HRMS)"
