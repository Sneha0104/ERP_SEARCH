from django.shortcuts import render
from .models import InvoiceDetail, InvoiceHead, Item, Supplier
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def invoice(request):
    queryset_head = InvoiceHead.objects.all()
    queryset_items = Item.objects.all()
    queryset_supplier = Supplier.objects.all()
    context = {
        'mats': queryset_supplier,
        'books': queryset_items,
        'lists': queryset_head,
    }
    return render(request, 'invoice/invoice.html', context)


@login_required
def invoiceDetail(request):
    flag = 1
    temp=1
    queryset_l = InvoiceHead.objects.all()
    queryset_list = InvoiceDetail.objects.all()
    # pr_no
    if 'INVOICE_NUMBER' in request.GET:
        ino = request.GET['INVOICE_NUMBER']
        if ino:
            flag = 0
            queryset_l = queryset_l.filter(invoice_no__exact=ino)
            queryset_list = queryset_list.filter(invoice_head__invoice_no__exact=ino)
    else:
        pass

    if 'INVOICE_DATE' in request.GET:
        invoice_date = request.GET['INVOICE_DATE']
        if invoice_date:
            flag = 0
            queryset_l = queryset_l.filter(invoice_date__exact=invoice_date)
            queryset_list = queryset_list.filter(invoice_head__invoice_date__exact=invoice_date)
    else:
        pass

        # supplier_code
    if 'SUPPLIER_CODE' in request.GET:
        supp_code = request.GET['SUPPLIER_CODE']
        if supp_code:
            flag = 0
            temp=0
            queryset_list = queryset_list.filter(supplier__supplier_code__icontains=supp_code)
    else:
        pass

    if 'DESCRIPTION' in request.GET:
        desc = request.GET['DESCRIPTION']
        if desc:
            flag = 0
            temp=0
            queryset_list = queryset_list.filter(item__item_description__icontains=desc)
    else:
        pass

    cont = {
        'lists': queryset_l,
        'posts': queryset_list

    }
    if flag == 0:
        if temp == 0:
            return render(request, 'invoice/invoice_dtl.html', cont)

        if temp == 1:
            return render(request, 'invoice/invoice_dtl1.html', cont)
    else:
        queryset_head = InvoiceHead.objects.all()
        queryset_items = Item.objects.all()
        queryset_supplier = Supplier.objects.all()
        context = {
            'mats': queryset_supplier,
            'books': queryset_items,
            'lists': queryset_head,
        }
        messages.success(request, f'Enter a value')
        return render(request, 'invoice/invoice.html',context)