from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomerProfileForm
from .models import Customer


@login_required
def create_profile(request):
    form = CustomerProfileForm()

    if request.method == "POST":
        form = CustomerProfileForm(request.POST)

        if form.is_valid():
            cleaned = form.cleaned_data
            first_name = cleaned.get('first_name')
            last_name = cleaned.get('last_name')
            address = cleaned.get('address')
            phone = cleaned.get('phone')
            user = request.user

            newCustomer = Customer(
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone=phone,
                user=user
            )

            newCustomer.save()

            return redirect("profile")

        else:
            return render(request, "customer/create_profile.html", {'form': form})

    else:
        return render(request, "customer/create_profile.html", {'form': form})


@login_required
def check_profile(request):
    user = request.user
    if hasattr(user, 'customer'):
        return redirect('profile')

    else:
        return redirect('create_profile')


@login_required
def get_profile(request):

    user = request.user
    if not hasattr(user, 'customer'):
        return redirect('create_profile')

    customer = request.user.customer

    requests_set = request.user.servicerequest_set.all()
    requests_available = True
    if len(requests_set) == 0:
        requests_available = False

    return render(request, "customer/profile.html", {
        'customer': customer,
        'req_available': requests_available,
        'requests': requests_set,
    })
