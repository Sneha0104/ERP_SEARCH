from django.shortcuts import render
from .models import Item,Uom
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def item(request):
    queryset_items = Item.objects.all()
    queryset_uom = Uom.objects.all()
    context = {
        'posts':queryset_uom,
        'books': queryset_items,
    }
    return render(request, 'items/item_head.html', context)


@login_required
def itemDetail(request):
    flag = 1
    queryset_list = Item.objects.all()

    if 'ITEM_CODE' in request.GET:
        item_code = request.GET['ITEM_CODE']
        if item_code:
            flag = 0
            queryset_list = queryset_list.filter(item_code__exact=item_code)
    else:
        pass

    if 'DESCRIPTION' in request.GET:
        desc = request.GET['DESCRIPTION']
        if desc:
            flag = 0
            queryset_list = queryset_list.filter(item_description__icontains=desc)
    else:
        pass

    if 'UOM' in request.GET:
        uom = request.GET['UOM']
        if uom:
            flag = 0
            queryset_list = queryset_list.filter(uom__uom__icontains=uom)
    else:
        pass

    cont = {

        'posts': queryset_list

    }
    if flag == 0:
        return render(request, 'items/item_dtl.html', cont)
    else:
        queryset_items = Item.objects.all()
        queryset_uom = Uom.objects.all()
        context = {
            'posts': queryset_uom,
            'books': queryset_items,
        }
        messages.success(request, f'Enter a value')
        return render(request, 'items/item_head.html',context)
