"""saulgadgets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from inspect import ismethoddescriptor
from django.contrib import admin
from django.urls import path

### apps urls views
from apps.core.views import frontpage, contactpage 
from apps.store.views import product_detail

urlpatterns = [
    # App: core
    path('', frontpage, name = 'frontpage'),
    path('contact/', contactpage, name = 'contactpage'),

    #App: Store
    path('<slug:slug>/', product_detail, name = 'product_detail'),

    path('admin/', admin.site.urls),
]
