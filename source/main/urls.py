"""main URL Configuration

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
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import *
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('user/all', UserListView.as_view(), name='user_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>delete', UserDeleteView.as_view(), name='user_delete'),

]