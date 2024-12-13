"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import main_page, ClassTemplate, func_template
from task3.views import platform3, products3, shopping_cart3
from task4.views import platform, products, shopping_cart
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_page),
    path('class/', ClassTemplate.as_view()),
    path('func/', func_template),

    path('platform3/', platform3),
    path('games3/', products3),
    path('cart3/', shopping_cart3),


    path('platform/', platform),
    path('games/', products),
    path('cart/', shopping_cart),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
]
