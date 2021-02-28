# membuat view function pada website
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def description(request, pk):
    products = get_object_or_404(Product, pk=pk)
    context = {'products': products}
    return render(request, 'store/description.html', context)


def spec(request):
    context = {}
    return render(request, 'store/spec.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Akun {username} telah berhasil dibuat! Silahkan masuk.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})
