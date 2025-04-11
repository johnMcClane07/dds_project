"""
URL configuration for dds_project project.

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
from dds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Для записей о ДДС
    path('cashflows/', views.cashflow_list, name='cashflow_list'),
    path('cashflows/create/', views.cashflow_create_or_edit, name='cashflow_create'),
    path('cashflows/edit/<int:pk>/', views.cashflow_create_or_edit, name='cashflow_edit'),
    path('cashflows/delete/<int:pk>/', views.cashflow_confirm_delete, name='cashflow_delete'),

    # Для статусов
    path('statuses/', views.status_list, name='status_list'),
    path('statuses/create/', views.status_create, name='status_create'),
    path('statuses/edit/<int:pk>/', views.status_edit, name='status_edit'),
    path('statuses/delete/<int:pk>/', views.status_delete, name='status_delete'),

    # Типы
    path('types/', views.type_list, name='type_list'),
    path('types/create/', views.type_create, name='type_create'),
    path('types/<int:pk>/edit/', views.type_edit, name='type_edit'),
    path('types/<int:pk>/delete/', views.type_confirm_delete, name='type_delete'),

    # Категории
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_confirm_delete, name='category_delete'),

    # Подкатегории
    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/create/', views.subcategory_create, name='subcategory_create'),
    path('subcategories/<int:pk>/edit/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategories/<int:pk>/delete/', views.subcategory_confirm_delete, name='subcategory_delete'),

]

