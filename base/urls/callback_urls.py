from django.urls import path
from base.views import callback_views

urlpatterns = [
    path('', callback_views.getPaymentResponse, name='paymentResponse'),
    path('create/', callback_views.createPaymentResponse, name='create-paymentResponse'),
    
]
