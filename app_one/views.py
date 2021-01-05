from django.shortcuts import render, redirect, HttpResponse
from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "amadon_main.html", context)


def purchase(request):
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
        request.session['total_charge'] = 0
        
    if request.POST['product_id'] == '1015':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 19.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['quantity'] = int(request.POST['quantity'])
        request.session['item'] = 'Dojo Tshirt'
        
    if request.POST['product_id'] == '1016':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 29.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['quantity'] = int(request.POST['quantity'])
        request.session['item'] = 'Dojo Sweater'
        
    if request.POST['product_id'] == '1017':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 4.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['quantity'] = int(request.POST['quantity'])
        request.session['item'] = 'Dojo Cup'
        
    if request.POST['product_id'] == '1018':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 49.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['quantity'] = int(request.POST['quantity'])
        request.session['item'] = 'Algorithm Book'
        
    return redirect('/checkout')


def checkout(request):
    return render(request, 'amadon_checkout.html')


def clear(request):
    request.session.clear()
    return redirect('/')