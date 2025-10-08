from django.shortcuts import get_object_or_404, redirect, render
from .models import Contact
from .forms import ContactForm


# Create your views here.
def home(request):
    return redirect('contacts-list')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp1/contact_list.html', {'contacts':contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'myapp1/contact_detail.html',{'contact':contact})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contacts-detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'myapp1/contact_form.html', {'form':form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts-detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'myapp1/contact_form.html', {'form':form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts-list')
    return render(request, 'myapp1/contact_confirm_delete.html', {'contact':contact})