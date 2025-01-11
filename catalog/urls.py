from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, ContactView


app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='product_list'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/<int:pk>', CatalogDetailView.as_view(), name='product_detail'),
]
