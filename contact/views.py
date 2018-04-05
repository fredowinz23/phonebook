from django.shortcuts import render, redirect
from .models import Contact

def view(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/index.html', { 'contact_list' : contact_list })

def create(request):
    return render(request, 'contact/create.html')

def create_post(request):
    contact = Contact()
    contact.name = request.POST['name']
    contact.phone = request.POST['phone']
    contact.save()

    return redirect('/contact')

def update(request, contactId):
    contact = Contact.objects.get(id = contactId)
    return render(request, 'contact/update.html', {'contact' : contact })

def update_post(request, contactId):
    contact = Contact.objects.get(id = contactId)
    contact.name = request.POST['name']
    contact.phone = request.POST['phone']
    contact.save()

    return redirect('/contact')

def delete_post(request, contactId):
    contact = Contact.objects.get(id = contactId)
    contact.delete()
    return redirect('/contact')
