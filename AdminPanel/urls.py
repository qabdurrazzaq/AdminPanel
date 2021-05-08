"""AdminPanel URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,re_path
from userfeatures import views as userfeatureviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userfeatureviews.user_view,name='user'),
    path('user/login/',userfeatureviews.login_view,name='login'),
    path('user/logout/',userfeatureviews.logout_view,name='logout'),
    path('user/add_new_user',userfeatureviews.add_new_user_view,name='add_new_user'),
    re_path(r'^ajax/add_new_user/$', userfeatureviews.add_new_user, name='create_user'),
    path('user/del_user',userfeatureviews.del_user_view,name='del_user_view'),
    re_path(r'^ajax/del_user/$', userfeatureviews.del_user, name='del_user'),
    path('user/view_all_users/',userfeatureviews.view_all_users_view,name='view_all_users'),
    path('user/all_users_stats/',userfeatureviews.all_users_stats_view,name='all_users_stats'),
    path('user/edit_user/',userfeatureviews.edit_user_view,name='edit_user'),
    re_path(r'^user/edit_user/(?P<username>[\w-]+)/$',userfeatureviews.edit_single_user,name='edit_single_user'),
    path('ajax/update_user/',userfeatureviews.update_user,name='update_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
