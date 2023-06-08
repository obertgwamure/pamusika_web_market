from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

#dashboard views

@login_required
def index(request):
    """This  Method uses a decorator to ensure that users can only access dashboard when logged in

        :param request: HTTP protocol request

        :returns: renders the dashboard/index.html file

        :rtype: render
    """
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })


