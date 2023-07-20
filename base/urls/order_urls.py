from django.urls import path
from base.views import order_views


urlpatterns = [
    path('', order_views.getOrders, name='orders'),
    path('add/', order_views.addOrderItems, name='orders-add'),
    path('myorders/', order_views.getMyOrders, name='myorders'),
    path('<str:pk>/deliver/', order_views.updateOrderToDelivered,
         name='order-delivered'),
    path('<str:pk>/', order_views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', order_views.updateOrderToPaid, name='pay'),

]
