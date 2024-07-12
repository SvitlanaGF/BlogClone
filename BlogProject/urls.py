
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog_app.urls")),
    path('accounts/login/$', views.auth_login, name='login'),
    path('accounts/logout/$', views.auth_logout, name='logout', kwargs={'next_page': '/'}, ),
]
