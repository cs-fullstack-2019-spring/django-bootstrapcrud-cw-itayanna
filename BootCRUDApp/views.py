from django.shortcuts import render, redirect, get_object_or_404
from .models import sellItem
from .forms import sellItemform


# Create your views here.


# function for index pageview
def index(request):
    allEntries = sellItem.objects.all()
    form = sellItemform(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context = {
        'allEntries': allEntries,
        'form': form
    }

    return render(request, 'BootCRUDApp/index.html', context)

# function in order to edit items in the database

def editItem(request, id):
    item = get_object_or_404(sellItem, pk=id)
    editForm = sellItemform(request.POST or None, instance=item)
    if request.method == "POST":
        if editForm.is_valid():
            editForm.save()
            return redirect('index')

    return render(request, 'BootCRUDApp/edit.html', {'editForm': editForm})

