from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('/<slug:slug>', views.home, name='prod_ct'),
    path('<slug:c_slug>/<slug:p-slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search')
    
    
]
