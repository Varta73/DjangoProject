from django.shortcuts import render, get_object_or_404
from  django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# def home(request):
#     return render(request, 'home.html')


class HomeProductListView(ListView):
    model = Product

# def contacts(request):
#     return render(request, 'contacts.html')


class CatalogListView(ListView):
    model = Product


# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)


class CatalogDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
