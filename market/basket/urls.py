from django.urls import path

from .views import BasketOfProductsView, Orders, OrderDetail, PaymentView

app_name = 'basket'

urlpatterns = [
    path('basket/', BasketOfProductsView.as_view(), name='basket'),
    path('cart/', BasketOfProductsView.as_view(), name='cart'),
    path("orders/", Orders.as_view()),
    path("orders/<int:pk>/", OrderDetail.as_view()),
    path("payment/<int:pk>/", PaymentView.as_view()),
]
