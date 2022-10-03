"""mylib URL Configuration

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
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage,name="homepage"),
    path('signup/', views.signuppage,name="signuppage"),
    path('login/', views.loginpage,name="loginpage"),
    path('logout/', views.logoutpage,name="logoutpage"),
    path('about-us/', views.about_us,name="aboutus"),
    path('viewbook/', views.viewbook,name="viewbookpage"),
    path('add-book/', views.add_book,name="addbook"),
    path('update-delete/', views.update_delete,name="update_delete"),
    path('update/<title>', views.update,name="update"),
    path('delete/<title>', views.delete_book,name="delete_book"),







]
