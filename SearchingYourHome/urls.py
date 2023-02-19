"""SearchingYourHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Room.views import *
from re import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('signup', signup,name='signup'),
    path('pay', pay,name='pay'),
    path('signin', signin,name='signin'),
    path('logout', Logout,name='logout'),
    path('search', Search,name='search'),
    path('contact', Contact,name='contact'),
    path('about', About,name='about'),
    path('view_user', View_User,name='view_user'),
    path('rent1', rent1,name='rent1'),
    path('img', Room_Img,name='img'),
    path('add_state', Add_State,name='add_state'),
    path('view_state', View_State,name='view_state'),
    path('view_dist', View_District,name='view_dist'),
    path('add_dist', Add_District,name='add_dist'),
    path('request', View_Request,name='request'),
    path('bookings', bookings,name='bookings'),
    path('user_detail', User_detail,name='user_detail'),
    path('all_ads', All_Ads ,name='alladd'),
    path('owner/(?P<pid>[0-9]+)', Owner_detail,name='owner'),
    path('edit_detail/(?P<data1>[0-9]+)/(?P<pid>[0-9]+)', Edit_detail,name='edit_detail'),
    path('change/(?P<data>[0-9]+)/(?P<pid>[0-9]+)', Change,name='change'),
    path('delete_detail/(?P<pid>[0-9]+)', delete_detail,name='delete'),
    path('edit_detail1/(?P<data>[0-9]+)', edit_detail1,name='edit_detail1'),
    path('edit_state/(?P<pid>[0-9]+)', Edit_State,name='edit_state'),
    path('room_img/(?P<pid>[0-9]+)', Add_Room_Img,name='room_img'),
    path('dist/(?P<dist>[0-9]+)', dist,name='dist'),
    path('rent/(?P<pid>[0-9]+)', rent,name='rent'),
    path('room/(?P<dist>[0-9]+)', room,name='room'),
    path('edit_user/(?P<pid>[0-9]+)', Edit_User,name='edit_user'),
    path('delete_user/(?P<pid>[0-9]+)', delete_user,name='delete_user'),
    path('delete_dist/(?P<pid>[0-9]+)', delete_dist,name='delete_dist'),
    path('delete_state/(?P<pid>[0-9]+)', delete_state,name='delete_state'),
    path('change_img/(?P<pid>[0-9]+)', Change_Img,name='change_img'),
    path('detail/(?P<dist>[0-9]+)', detail,name='detail'),
    path('detail1/(?P<dist>[0-9]+)', detail1,name='detail1'),
    path('customer-address',customer_address_view,name='customer-address'),
    path('payment-success',payment_success_view,name='payment-success'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
