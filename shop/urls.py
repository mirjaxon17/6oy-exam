from django.urls import path
from .views import ShopListView, ShopDetailView, ShopDetailOrg, CartListView, ChackOutView, TestiminialView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop/<int:id>/', ShopDetailView.as_view(), name='shop-detail'),
    path('shop/detail/<int:id>/', ShopDetailOrg.as_view(), name='shop-detail_org'),
    path('shop/card/', CartListView.as_view(), name='cart'),
    path('shop/card/chack/', ChackOutView.as_view(), name='chackout'),
    path('testiminial', TestiminialView.as_view(), name='client'),
]