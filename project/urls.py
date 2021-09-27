"""project URL Configuration

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
from django.urls import path
from  app.views import home, form, create, view, edit, update, delete, viewprod, homepro, novoproduto
#editprod, updateprod, deleteprod,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

    #path('createprod/', createprod, name='createprod'),
    #path('viewprod/<int:fk>/', viewprod, name='viewprod'),
    #path('updateprod/<int:pk>/', updateprod, name='updateprod'),
    path('empresa/<int:empresa_ip>/produtos/', homepro, name='homepro'),
    path('empresa/<int:empresa_ip>/produtos/novo', novoproduto, name='novoproduto'),

    #path('editprod/<int:fk>/', editprod, name='editprod'),
    #path('updateprod/<int:fk>/', updateprod, name='updateprod'),
    #path('deleteprod/<int:fk>/', deleteprod, name='deleteprod'),

    ]
