from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Item, Creator
from .forms import ItemForm, ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries."""

    products = Product.objects.all()
    query = None
    categories = None
    creators = None
    sort = None
    direction = None

    # If using seach bar or menu selections
    if request.GET:
        # SEARCH ENTRY FUNCTIONALITY
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter\
                               any search criterion.")
                return redirect(reverse('products'))

            # Search term in product name or description.
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # CATEGORY SELECTION FUNCTIONALITY
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(item_id__category_id__category_tag__in=categories)
            categories = Category.objects.filter(category_tag__in=categories)

        # CREATOR SELECTION FUNCTIONALITY
        if 'creator' in request.GET:
            creators = request.GET['creator'].split(',')
            products = products.filter(item_id__creator_id__name__in=creators)
            creators = Creator.objects.filter(name__in=creators)

        # SORTING FUNCTIONALITY
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'item_id__category_id'

            if sortkey == 'price':
                sortkey = 'item_id__unitcost'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_creators': creators,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required()
def add_item(request):
    """ Add an item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Superuser authorisation required to perform this action.')
        return redirect(reverse('products'))
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new item.')
            return redirect(reverse('add_item'))
        else:
            messages.error(request, 'Failed to add item.\
                           Check form for errors and try again.')
    else:
        form = ItemForm()

    form = ItemForm()
    template = 'products/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_item(request, item_id):
    """ Edit an item in the shop. """
    if not request.user.is_superuser:
        messages.error(request, 'Superuser authorisation required \
                       to perform this action.')
        return redirect(reverse('products'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item details updated.')
            return redirect(reverse('edit_item', args=[item.id]))
        else:
            messages.error(request, 'Failed to update item.\
                           Check form is valid.')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing item named: {item.name}')

    template = 'products/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required()
def add_product(request):
    """ Add a product to the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Superuser authorisation required \
                       to perform this action.')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new product.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product.\
                           Check form for errors and try again.')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_product(request, product_id):
    """ Edit a product in the shop. """
    if not request.user.is_superuser:
        messages.error(request, 'Superuser authorisation required \
                       to perform this action.')
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product details updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                           Check form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing product no. {product.id}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def delete_product(request, product_id):
    """ Delele a product from the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Superuser authorisation required \
                       to perform this action.')
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('products'))
