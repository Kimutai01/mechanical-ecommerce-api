from django.urls import path
from base.views import order_views


urlpatterns = [
    path('add/', order_views.addOrderItems, name='orders-add'),
    path('myorders/', order_views.getMyOrders, name='myorders'),
    path('<str:pk>/', order_views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', order_views.updateOrderToPaid, name='pay'),

]
