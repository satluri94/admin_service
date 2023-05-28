from django.urls import path
from . import views


urlpatterns = [
    path('admdash/menuitem/add/', views.addMenuItem, name='addMenuItem'),
    path('admdash/menuitem/update/', views.updateMenuItem, name='updateMenuItem'),
    path('admdash/menuitem/delete/', views.deleteMenuItem, name='deleteMenuItem'),
    path('admdash/menuitems/', views.listMenuItems.as_view(), name='listMenuItems'),
    path('admdash/availability/', views.getAvailability.as_view(), name='getAvailability'),
    path('admdash/availability/toggle/', views.toggleAvailability, name='toggleAvailability'),
    path('admdash/timings/', views.setTimings, name='setTimings'), #post
    path('admdash/orders/', views.getNewOrders.as_view(), name='getNewOrders'), #get
    path('admdash/orders/accept/', views.acceptOrder, name='acceptOrder'),  #post
    path('admdash/orders/status/', views.getAcceptedOrders.as_view(), name='getAcceptedOrders'), #get
    path('admdash/orders/place/', views.placeNewOrder, name='placeNewOrder')  #post
]
