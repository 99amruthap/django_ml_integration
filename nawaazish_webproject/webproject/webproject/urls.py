"""webproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from webapp.views import (JoinFormView, ContactView, ContactFormView, GalleryCreateView, AboutCreateView,
    EventCreateView, contact_show, DonateCreateView, JoinUsIndexCreateView, ContactUsCreateView, CrewUsCreateView )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', AboutCreateView.as_view(), name='about'),
    path('contact/', contact_show, name='contact'),
    path('donate/', DonateCreateView.as_view(), name='donate'),
    path('gallery/', GalleryCreateView.as_view(), name='gallery'),
    path('crew/', CrewUsCreateView.as_view(), name='crew'),
    path('event/', EventCreateView.as_view(), name='event'),
    path('index/', JoinUsIndexCreateView.as_view(), name='join_us'),
    path('contactUs/', ContactView.as_view(), name='contact_us'),
    path('contactUs/create/', ContactFormView.as_view(), name='create'),
    path('contactUs/join/', JoinFormView.as_view(), name='join'),
]





