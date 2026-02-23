from django.urls import path
from .views import (
    CategoryListView, ProductListView,
    ProductDetailView, ReviewCreateView, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]
