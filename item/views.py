from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, Category
from .forms import NewItemForm, EditItemForm

# Item views

def browse_items(request):
    """This  creates a view for the users to browse items

        :param request: HTTP protocol request

        :returns: renders the item/browse_items.html file

        :rtype: render"""
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if query:
        # the double underscore is used in name__icontains to search for name that
        # contains the string in query
        # The Q from django.db.models is used to query over multiple fields
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = Item.objects.filter(category_id=category_id)

    return render(request, 'item/browse_items.html',{
            'items': items,
            'query': query,
            'categories': categories,
            'category_id': int(category_id)
        })


def detail(request, pk):
    """This  creates a view for the users to see a selected item's details

        :param request: HTTP protocol request

        :returns: renders the 'item/detail.html' file

        :rtype: render
    """
    #getting item from database
    item = get_object_or_404(Item, pk=pk)

    #getting a list of related items from database
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        })


@login_required
def new(request):
    """This  creates a view for the users add new items.
    A Django decorator is used to ensure the user is logged in first.

        :param request: HTTP protocol request

        :returns: renders the 'item/item_form.html' file

        :rtype: render
    """
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False) #not commiting to database yet Created_by field is required
            item.created_by = request.user #user is always required by the login_decorator
            item.save()

            # directing user to the detail page of the created item.
            return redirect('item:detail', pk=item.id)

    form = NewItemForm()

    return render(request, 'item/item_form.html', {
            'form_action': 'new',
            'form': form,
            'title': 'New Item',
        })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk,created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk,created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)

        if form.is_valid():
            item.save()

            # directing user to the detail page of the created item.
            return redirect('item:detail', pk=item.id)

    form = EditItemForm(instance=item)

    return render(request, 'item/item_form.html', {
            'form_action': 'edit',
            'item': item,
            'form': form,
            'title': 'Edit Item',
        })