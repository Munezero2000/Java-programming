from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Menu


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = Menu.objects.all().order_by('name')
    return render(request, 'menu.html', {'main': menu_data})


def display_menu_items(request, pk):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request, 'menu_item.html', {'menu_item': menu_item})
