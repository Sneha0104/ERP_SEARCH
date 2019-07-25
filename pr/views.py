from django.shortcuts import render
from .models import PRDetail, PRHead, Item, Supplier
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def prHead(request):
    queryset_head = PRHead.objects.all()
    queryset_detail = PRDetail.objects.all()
    queryset_items = Item.objects.all()
    queryset_supplier = Supplier.objects.all()
    context = {
        'mats': queryset_supplier,
        'books': queryset_items,
        'lists': queryset_head,
        'posts': queryset_detail
    }
    return render(request, 'pr/pr_head.html', context)


@login_required
def prDetail(request):
    flag = 1
    temp = 1
    queryset_l = PRHead.objects.all()
    queryset_list = PRDetail.objects.all()

    # pr_no
    if 'PR_NUMBER' in request.GET:
        pno = request.GET['PR_NUMBER']
        if pno:
            flag = 0
            queryset_l = queryset_l.filter(pr_no__exact=pno)
            queryset_list = queryset_list.filter(pr_head__pr_no__exact=pno)

    else:
        pass

    # supplier_code
    if 'SUPPLIER_CODE' in request.GET:
        supp_code = request.GET['SUPPLIER_CODE']
        if supp_code:
            flag = 0
            temp = 0
            queryset_list = queryset_list.filter(supplier__supplier_code__icontains=supp_code)

    else:
        pass

    if 'DESCRIPTION' in request.GET:
        desc = request.GET['DESCRIPTION']
        if desc:
            flag = 0
            temp = 0
            queryset_list = queryset_list.filter(item__item_description__icontains=desc)

    else:
        pass

    if 'PR_DATE' in request.GET:
        pr_date = request.GET['PR_DATE']
        if pr_date:
            flag = 0
            queryset_l = queryset_l.filter(pr_date__exact=pr_date)
            queryset_list = queryset_list.filter(pr_head__pr_date__exact=pr_date)
    else:
        pass

    if 'APPROVED_DATE' in request.GET:
        appr_date = request.GET['APPROVED_DATE']
        if appr_date:
            flag = 0
            queryset_l = queryset_l.filter(approved_date__exact=appr_date)
            queryset_list = queryset_list.filter(pr_head__approved_date__exact=appr_date)
    else:
        pass


    cont = {
        'lists': queryset_l,
        'posts': queryset_list,

         }
    if flag == 0:
        if temp == 0:
            return render(request, 'pr/pr_dtl.html', cont)

        if temp==1:
            return render(request, 'pr/pr_dtl1.html', cont)
    else:
        queryset_head = PRHead.objects.all()
        queryset_detail = PRDetail.objects.all()
        queryset_items = Item.objects.all()
        queryset_supplier = Supplier.objects.all()
        context = {
            'mats': queryset_supplier,
            'books': queryset_items,
            'lists': queryset_head,
            'posts': queryset_detail
        }
        messages.success(request, f'Enter a value')
        return render(request, 'pr/pr_head.html',context)


