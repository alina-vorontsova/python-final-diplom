"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.views import SupplierUpdate, ShopView, CategoryView, ProductView, OrderView, OrderInfoView, BasketView, OrderConfirmation, UserRegisterView, Login, ContactView


router = DefaultRouter()
router.register(r'shops', ShopView, basename='shops')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'products', ProductView, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('get_contact/', ContactView.as_view(), name='get_contact_info'),
    path('update/<str:file_name>/', SupplierUpdate.as_view(), name='update_products'),
    # path('shops/', ShopView.as_view({'get': 'list'}), name='all_shops'),
    # path('categories/', CategoryView.as_view({'get': 'list'}), name='all_categories'),
    # path('products/', ProductView.as_view({'get': 'list'}), name='all_products'),
    path('orders/', OrderView.as_view(), name='user_orders_list'),
    path('orders/<int:order_id>/', OrderInfoView.as_view(), name='order_info'), 
    path('basket/', BasketView.as_view(), name='basket'),
    path('order_confirmation/', OrderConfirmation.as_view(), name='order_confirmation'),
    path('', include(router.urls))
]