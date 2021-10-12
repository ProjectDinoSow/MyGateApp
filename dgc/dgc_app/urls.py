from django.urls import path
import views

urlpatterns = [
    path('master', views.master_login.as_view({
        'post': 'master_create',
    })),
    path('master/<str:pk>', views.master_login.as_view({
        'put': 'master_update',
        'delete': 'master_del',
    })),
    path('master/apartments', views.apartment_create.as_view({
        'get': 'app_views',
        'post': 'app_create',
    })),
    path('master/apartments/<str:pk>', views.apartment_create.as_view({
        'get': 'specify_app_views',
        'put': 'app_update',
        'delete': 'app_delete',
    })),
    path('master/admins', views.admin_register.as_view({
        'get': 'admin_views',
        'post': 'admin_create',
    })),
    path('master/admins/<str:pk>', views.admin_register.as_view({
        'get': 'specify_admin_views',
        'put': 'admin_update',
        'delete': 'admin_del',
    }))
]
