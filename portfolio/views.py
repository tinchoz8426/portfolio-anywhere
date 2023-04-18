from django.shortcuts import render
from django.contrib import messages

from .models import UserData, Portfolio, Contact
from .forms import ContactForm

# Create your views here.
def index(request):

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            messages.success(request, "Muchas gracias por tu contacto")
            
            info = contact_form.cleaned_data

            contact = Contact(name=info['name'], message=info['message'], email=info['email'])

            contact.save()

            contact_form = ContactForm()
        
    else:
        contact_form = ContactForm()

    user_data = UserData.objects.first()
    portfolios = Portfolio.objects.all()

    context = {
        "user_data": user_data,
        "portfolios": portfolios,
        "contact_form": contact_form,
    }

    return render(request, "portfolio/index.html", context)