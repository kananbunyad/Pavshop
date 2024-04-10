from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout,get_user_model, views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm,User_EditForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from account.tokens import account_activation_token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from account.forms import ResetForm
from checkout.models import ShoppingCart


User = get_user_model()


# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            user=form.save()
            ShoppingCart.objects.create(user=user)
            current_site = get_current_site(request)
            subject = f'Activate Your {current_site.domain} Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect("account:login")
    context = {"form": form}
    return render(request, "register.html", context=context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        # user.profile.email_confirmed = True
        user.save()
        return redirect('account:login')
    else:
        return render(request, 'account_activation_invalid.html')


    

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                django_login(request, user)
                return redirect(reverse('core:home'))
            else:
                form.add_error(None, "Invalid username or password")

    context = {"form": form}
    return render(request, "login.html", context)




@login_required(login_url=reverse_lazy("account:login"))
def logout(request):
    django_logout(request)

    return redirect("account:login")


def reset_password(request, uidb64,token):
    form = ResetForm()
    if request.method == "POST":
        form = ResetForm(request.POST)
        if form.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect(reverse_lazy("account:login"))

    return render(request, 'reset_password.html', {'form':form})
        



def forget_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                user=User.objects.get(email=form.cleaned_data['email'])
                current_site = get_current_site(request)
                subject = f'Reset Your {current_site.domain} Password'
                print(user)
                message = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
                user.email_user(subject,message)
                
            
            messages.success(request, 'Password reset link has been sent to your email.')

    else:
        form = PasswordResetForm()

    return render(request, 'forget_password.html', {'form': form})





class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class=User_EditForm
    model = User
    template_name = 'user_profile.html'
    
    success_url = reverse_lazy('core:home')  

    def get_object(self, queryset=None):
        # Get the user's profile
        return self.request.user
    def get_success_url(self) -> str:
        print(self.request.POST)
        return super().get_success_url()



  