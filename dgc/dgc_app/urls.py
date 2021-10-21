from django.urls import path
from .views import master_login, apartment_create, admin_register

urlpatterns = [
    path('master', master_login.as_view({
        'post': 'master_create',
        'get': 'master_views',
    })),
    path('master/<str:pk>', master_login.as_view({
        'post': 'login_masteruser',
        'get': 'logout_masteruser',
        'put': 'master_update',
        'delete': 'master_del',
    })),
    path('master/apartments', apartment_create.as_view({
        'get': 'app_views',
        'post': 'app_create',
    })),
    path('master/apartments/<str:pk>', apartment_create.as_view({
        'get': 'specify_app_views',
        'put': 'app_update',
        'delete': 'app_delete',
    })),
    path('master/admins', admin_register.as_view({
        'get': 'admin_views',
        'post': 'admin_create',
    })),
    path('master/admins/<str:pk>', admin_register.as_view({
        'get': 'specify_admin_views',
        'put': 'admin_update',
        'delete': 'admin_del',
    }))
]

