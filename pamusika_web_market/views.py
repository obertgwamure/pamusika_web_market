from django.shortcuts import render, redirect
from item.models import Category, Item
from . forms import SignupForm

# Pamusika Web Market Views
def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()

    return render(request, 'pamusika_web_market/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'pamusika_web_market/contact.html')

def signup(request):
    # handling submitting of signup form
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
        
    form = SignupForm()

    return render(request, 'pamusika_web_market/signup.html', {'form': form})

#def newitem(request)