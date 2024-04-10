from django.shortcuts import render,redirect
from django.contrib import messages
from product.models import Product,ProductVersion
from django.views.generic import TemplateView
from product.forms import CommentForm


def products(request):
    products = ProductVersion.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product-list.html',context=context)


def product_detail(request,slug):
    product_detail = ProductVersion.objects.get(slug=slug)
    form=CommentForm()
    
    if request.method == "POST":
        form = CommentForm(data=request.POST)

        if form.is_valid():

            user= form.save(commit=False)
            user.user = request.user 

            user.product_version=product_detail
            user.raiting=request.POST.get("rating")
            user.save()

            messages.add_message(request, messages.SUCCESS, "Comment sent successfully")
            return redirect('product:product-detail',slug=slug)
    context = {
    
        'product_detail': product_detail,
        'form' : form,
    }
    return render(request, 'product-detail.html',context=context)




class WishlistView(TemplateView):

    template_name="wishlist.html"


