"""CityBus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Citybus1 import views
urlpatterns = [
    path('', views.Auth),
	path('reg/', views.Reg),
	path('user/', views.user),
	path('user/viewBT/', views.viewBT),
	path('user/book/', views.buyT),
	path('user/book/findz/', views.findz),
	path('admin/', views.admin),
	path('admin/addbus/', views.addbus),
	path('admin/adddri/', views.adddri),
	path('admin/addschint/', views.addschint),
	path('admin/viewD/', views.viewD),
	path('admin/viewB/', views.viewB),
	path('admin/viewSint/viewTint/', views.viewTint),
	path('admin/viewSint/', views.viewSint),
	path('logout/', views.logout),
	
]
