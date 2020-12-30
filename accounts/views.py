from django.shortcuts import render, redirect
# Create your views here.
from .models import *
from .forms import OrderForm


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = Order.objects.filter(status='delivered').count()
    pending = Order.objects.filter(status='pending').count()
    context = {'orders':orders, 'customers':customers, 'total_customers':total_customers, 'total_orders':total_orders, 'delivered': delivered, 'pending':pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    order_count = order.count()
    context = {'customer':customer, 'order':order, 'order_count':order_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect("/")
    context = {'items': order}
    return render(request, 'accounts/delete.html', context)