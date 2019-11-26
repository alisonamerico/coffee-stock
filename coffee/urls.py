"""coffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

"""
 - path('rest-auth/', include('rest_auth.urls')),

Django-rest-auth library provides a set of REST API endpoints for registration, authentication
(including social media authentication), password reset, retrieve and update user details, etc.
By having these API endpoints, your client apps such as AngularJS, iOS, Android, and others can
communicate to your Django backend site independently via REST APIs for user management.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/', include('coffee.api.urls')),
]
