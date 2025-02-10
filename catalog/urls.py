from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductsByCategoryView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='product_list'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/<int:pk>', cache_page(60)(CatalogDetailView.as_view()), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/', CategoryListView.as_view(), name='category_form'),
    path('category/<int:pk>/product/', ProductsByCategoryView.as_view(), name='products_by_category'),
]
