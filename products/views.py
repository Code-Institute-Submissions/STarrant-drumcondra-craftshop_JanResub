from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries."""

    products = Product.objects.all()
    query = None
    categories = None

    # If using seach bar or menu selections
    if request.GET:
        # Return search results if user enters search criterion into search form.
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criterion.")
                return redirect(reverse('products'))

            # Search term in product name or description.
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
        # Return filtered results if
        if category in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
