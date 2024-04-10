from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from core.forms import ContactForm
from core.models import ProductVersion
from .tasks import export 


def home(request):
    NewProducts = ProductVersion.objects.all().order_by("-created_at")
    popular_products=ProductVersion.objects.all()

    context = {
    
        'newproducts': NewProducts,
        "popular_products":popular_products
    }
    return render(request, 'index.html',context=context)


def contact(request):  
    form = None
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Message sent successfully")
            return redirect('core:contact')
            
    elif request.method == "GET":
        form = ContactForm()

    context = {
        "form": form
    }
    return render(request, 'contact.html', context=context)


def about_us(request):
    
    return render(request, 'about-us.html')


def export_view(request):
    export.delay()
    return HttpResponse("Exporting")


def product_home(request):
    product_home = ProductVersion.objects.get()

    context = {
    
        'product': product_home,
    }
    return render(request, 'index.html',context=context)