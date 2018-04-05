from django.shortcuts import render

from .models import Contact

def view(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/index.html', { 'contact_list' : contact_list })

def create(request):
    return render(request,'contact/create.html')

def create_post(request):
    contact = Contact()
    contact.name = request.POST['name']
    contact.phone = request.POST['phone']
    contact.save()
    return render(request, 'contact/create.html')
