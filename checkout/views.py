from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BillingForm
from .models import ShoppingCart
from django.contrib.auth.decorators import login_required

# Create your views here.

class CartView(TemplateView):

    template_name="shopping-cart.html"

    

def payment(request):
    user_cart = get_object_or_404(ShoppingCart, user=request.user) 
    context={
        "cart":user_cart
    }



    return render(request,"payment.html",context)


@login_required
def billingaddress(request):
    user_cart = get_object_or_404(ShoppingCart, user=request.user)  
    form = BillingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.cart_id = user_cart 
            billing_address.save()
            messages.add_message(request, messages.SUCCESS, "Billing address added successfully")
            return redirect('checkout:payment')  
    else:
        form = BillingForm() 

    context = {
        "form": form
    }
    return render(request, 'checkout.html', context=context)
