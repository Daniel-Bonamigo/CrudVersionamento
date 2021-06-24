from django.shortcuts import render, redirect
from .models import produtos
from .forms import Productform

def list_produtos(request):
    produtos = Product.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def create_produtos(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_produtos')

    return render(request, 'products-form.html', {'form': form})

