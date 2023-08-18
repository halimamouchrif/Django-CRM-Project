from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name="home" ),
    path('logout/',views.logout_user, name="logout" ),
    path('register/',views.register_user, name="register" ),
    path('customer/<int:pk>',views.customer_record, name="customer_record" ),
    path('customer_delete/<int:pk>',views.customer_delete, name="customer_delete" ),
    path('customer_add/',views.customer_add, name="customer_add" ),
    path('customer_update/<int:pk>',views.customer_update, name="customer_update" ),
]
