from django.conf.urls import url
from django.urls import path
from QLVB2_APP import views
from .views import *
from offenses.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'QLVB2_APP'

urlpatterns = [
    url('register/', views.register, name='register'),
    url('login/', views.login, name='login'),
    url('logoutUser/', views.logoutUser, name='logout'),

    url(r'^$',views.index, name='index'),
    url(r'^congtacchuyenmon/$', views.congtacchuyenmon, name='congtacchuyenmon'),
    url(r'^tongsocongviec/$',views.tongsocongviec, name='tongsocongviec'),
    url(r'^hoanthanh/$', views.hoanthanh, name='hoanthanh'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^dangthuchien/$', views.dangthuchien, name='dangthuchien'),
    url(r'^chamtiendo/$', views.chamtiendo, name='chamtiendo'),
    url(r'^giahan/$', views.giahan, name='giahan'),
    url(r'^nhapdulieuchuyenmon/$', views.nhapdulieu_chuyenmon, name='nhapdulieu_chuyenmon'),
    url(r'^bangcap/$', views.bangcap, name='bangcap'),
    url(r'^taisan/$', views.taisan, name='taisan'),
    url(r'^dulieubaocaotuan/$', views.dulieubaocaotuan, name='dulieubaocaotuan'),


    path('edit_congviec/<str:pk>/', views.edit_congviec, name="edit_congviec"),
    path('delete_congviec/<str:pk>/', views.delete_congviec, name="delete_congviec"),

    path('edit_taisan/<str:pk>/', views.edit_taisan, name="edit_taisan"),
    path('delete_taisan/<str:pk>/', views.delete_taisan, name="delete_taisan"),

    path('edit_bangcap/<str:pk>/', views.edit_bangcap, name="edit_bangcap"),
    path('delete_bangcap/<str:pk>/', views.delete_bangcap, name="delete_bangcap"),

    path('edit_bctuan/<str:pk>/', views.edit_bctuan, name="edit_bctuan"),


    url(r'^csv/$', views.export_csv, name='export_csv'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
