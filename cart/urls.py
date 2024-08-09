from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails/',views.car_details,name='cartDetails'),
    path("add/<int:product_id>/",views.add_cart , name="addcart"),
    path("cart_decrement/<int:product_id>/",views.min_cart , name="cart_decrement"),
    path("remove/<int:product_id>/",views.car_delete , name="remove"),
    
]
