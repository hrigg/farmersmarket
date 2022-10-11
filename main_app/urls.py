from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name="about"),
    path('markets/', views.MarketList.as_view(), name="market_list"),
    path('markets/<int:pk>', views.MarketDetail.as_view(), name="market_detail"),
    path('markets/<int:pk>/update', views.MarketUpdate.as_view(), name="market_update"),
    path('markets/new', views.MarketCreate.as_view(), name="market_create"),
    path('vendors/new', views.VendorCreate.as_view(), name="vendor"),
    path('vendors/<int:pk>', views.VendorDetail.as_view(), name="vendor_detail"),
    path('markets/<int:pk>/vendors/<int:vendor_pk>/', views.MarketVendorAssoc.as_view(), name="market_vendor_assoc"),
]