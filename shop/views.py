from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import Http404
from decimal import Decimal
from .models import Product
from .cart import Cart


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def detail(request, id, title: str):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, "detail.html", context)


def store(request):
    category = request.GET.get('category')
    if category is not None:
        products = Product.objects.filter(category__title=category)
        return render(request, "store.html", {'products': products})
    products = Product.objects.all()
    return render(request, "store.html", {'products': products})


def checkout(request):
    return render(request, "checkout.html")


@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart')
    if not cart:
        cart = request.session['cart'] = {}
    if product_id in cart:
        update = request.POST.get('update')
        if update=='1':
            cart[product_id]['quantity'] = int(quantity)
        else:
            cart[product_id]['quantity'] += int(quantity)
    else:
        cart[product_id] = {
            'quantity': int(quantity),
            'price': str(product.price),
        }
    request.session.modified = True

    return redirect(reverse('shop:cart_detail'))


def cart_detail(request):
    cart = request.session.get('cart')
    if cart:
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
        return render(request, 'cart_detail.html', {'cart': cart})
    else:
        return render(request, 'cart_detail.html',{'cart_is_empty':True})


def remove_from_cart(request, product_id):
    if Product.objects.filter(id=product_id).exists():
        cart = request.session['cart']
        if cart:
            product_id = str(product_id)
            if product_id in cart:
                del cart[product_id]
                request.session.modified = True
        return redirect(reverse('shop:cart_detail'))
    raise Http404('محصول مورد نظر یافت نشد')


