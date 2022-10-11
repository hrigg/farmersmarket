from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name="about"),
    path('markets/', views.MarketList.as_view(), name="market_list"),
    path('markets/<int:pk>', views.MarketDetail.as_view(), name="market_detail"),
    path('markets/<int:pk>/update', views.MarketUpdate.as_view(), name="market_update"),
    path('markets/<int:pk>/delete', views.MarketDelete.as_view(), name="market_delete"),
    path('markets/new', views.MarketCreate.as_view(), name="market_create"),
    path('vendors/', views.VendorList.as_view(), name="vendor_list"),
    path('vendors/new', views.VendorCreate.as_view(), name="vendor"),
    path('vendors/<int:pk>', views.VendorDetail.as_view(), name="vendor_detail"),
    path('vendors/<int:pk>/products/new', views.ProductCreate.as_view(), name="product_create"),
    path('markets/<int:pk>/vendors/<int:vendor_pk>/', views.MarketVendorAssoc.as_view(), name="market_vendor_assoc"),
    path('products/<int:pk>', views.ProductDetail.as_view(), name="product_detail"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]