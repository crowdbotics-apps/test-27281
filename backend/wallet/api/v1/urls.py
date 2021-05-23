from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PaymentTransactionViewSet,
    PaymentMethodViewSet,
    TaskerWalletViewSet,
    TaskerPaymentAccountViewSet,
    CustomerWalletViewSet,
)

router = DefaultRouter()
router.register("paymenttransaction", PaymentTransactionViewSet)
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("customerwallet", CustomerWalletViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("taskerwallet", TaskerWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
