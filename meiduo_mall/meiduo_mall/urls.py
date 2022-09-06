"""meiduo_mall URL Configuration

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

from django.http import HttpResponse

def log(request):
    #1. import
    import logging
    #2. create log machine
    logger=logging.getLogger('django')
    #3. use log machine method save log
    logger.info('user login')
    logger.warning('redis cache insuffient')
    logger.error('the log is not exist')
    logger.debug('~~~~~~~~~~~~')
    return HttpResponse('log')

urlpatterns = [
    path('admin/', admin.site.urls),
    #import users app route
    path('',include('apps.users.urls')),

]

#test go