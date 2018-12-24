"""database URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from second_book_server import views
urlpatterns = [
    #超级管理员接口
    path('admin', admin.site.urls),

    #用户注册接口
    path('registe',views.register),

    #登录接口
    path('log',views.login),
    path('logout',views.logout),

    #主页相关接口
    path('index',views.index),
    path('',views.index),

    #活动的相关接口
    path('activity',views.activity),


    #公告的相关接口
    path('announcement',views.announcement),

    #货物相关接口
    path('goods',views.goods),
    path('goods_list',views.goods_list),
    path('publish',views.publish),
    path('pubanno',views.pubanno),

    #卖家系统相关系统
    path('seller',views.seller),

    #上传媒体文件的接口
    path('upload',views.upload),

    #管理员相关接口
    path('admin_activity',views.admin_activity),
    path('admin_anno',views.admin_anno),
    path('admin_coupon',views.admin_coupon),
    path('admin_goods',views.admin_goods),
    path('admin_user',views.admin_user),
    path('admin_index', views.admin_index),
    path('admin_anno_list',views.admin_anno_list),
    path('admin_search_anno',views.admin_search_anno),
    path('admin_anno_delete',views.admin_anno_delete),
    path('admin_publish_activity',views.admin_publish_activity),
    path('admin_activity_list',views.admin_activity_list),
    path('admin_search',views.admin_search),
    path('admin_user_list',views.admin_user_list),
    path('admin_user_delete',views.admin_user_delete),
    path('admin_user_latest_login',views.admin_user_latest_login),
    path('goods_delete',views.delete_goods),

    #聊天相关接口
    path('chat',views.chat),

    #用户中心相关接口
    path('mycoupon',views.mycoupon),
    path('mygoods',views.mygoods),
    path('myorder',views.myorder),
    path('profile',views.profile),
    path('validation',views.validation),

    #订单接口
    path('ordersheet',views.ordersheet),
    path('shopping_cart',views.shopping_cart),
    path('admin_publish',views.admin_publish),
    path('admin_activity_delete',views.admin_activity_delete),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
