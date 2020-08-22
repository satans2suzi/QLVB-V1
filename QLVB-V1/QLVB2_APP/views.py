from django.shortcuts import render, redirect, get_object_or_404
from QLVB2_APP.models import themmoi_m, tiendo, thuchien_m, bangcap_m, taisan_m, bctuan_m, duongdan_m
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from . import forms
import datetime
from datetime import timedelta
from .filters import tongsofilter
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as dj_login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import csv
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('QLVB2_APP:index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Tài khoản được đăng ký thành công' + user)

                return redirect('QLVB2_APP:login')

        context = {'form':form}
        return render(request, 'QLVB2_APP/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('QLVB2_APP:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username =username, password = password)
            if user is not None:
                dj_login(request, user)
                return redirect ('QLVB2_APP:index')
            else:
                messages.info(request, 'Tài khoản hoặc mật khẩu không đúng')

        context={}
        return render(request, 'QLVB2_APP/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('QLVB2_APP:login')


# @login_required(login_url='QLVB2_APP:login')
def index(request):
    orderlist_=['tiendo_name', 'ketthuc_name']
    danhmuc_congtacchuyenmon = themmoi_m.objects.all().order_by(*orderlist_)
    tiendo_data = tiendo.objects.all()
    thuchien_data = thuchien_m.objects.all()
    bctuan_data = bctuan_m.objects.order_by('-stt_bct')[:1]
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    soluong = danhmuc_congtacchuyenmon.count()
    cham = danhmuc_congtacchuyenmon.filter(tiendo_name='3').count()
    hoanthanh = danhmuc_congtacchuyenmon.filter(tiendo_name='2').count()
    dangthuchien = danhmuc_congtacchuyenmon.filter(tiendo_name='1').count()
    giahan = danhmuc_congtacchuyenmon.filter(tiendo_name='4').count()

    # view pages
    page = request.GET.get('page', 1)
    paginator = Paginator(danhmuc_congtacchuyenmon, 5)
    try:
        page_hienthi = paginator.page(page)
    except PageNotAnInteger:
        page_hienthi =  paginator.page(1)
    except EmptyPage:
        page_hienthi = paginator.page(paginator.num_pages)

    return render(request, 'QLVB2_APP/index.html',context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                                                            'soluong':soluong, 'cham':cham, 'hoanthanh':hoanthanh,
                                                            'dangthuchien':dangthuchien,'giahan':giahan,
                                                            'Myfilter':Myfilter, 'tiendo_data': tiendo_data,
                                                            'thuchien_data':thuchien_data, 'page_hienthi':page_hienthi,
                                                            'bctuan_data':bctuan_data})
# export csv
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="solieu.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['stt_name', 'doidung_name', 'thuchien_name', 'ketthuc_name', 'Ghichu_name'])
    danhmuc_congtacchuyenmon = themmoi_m.objects.all().order_by('-stt_name')
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    danhmuc_congtacchuyenmon = danhmuc_congtacchuyenmon.values_list('stt_name', 'doidung_name', 'thuchien_name', 'ketthuc_name', 'Ghichu_name')
    for doidung_name in danhmuc_congtacchuyenmon:
      writer.writerow(doidung_name)
    return response

# Bằng cấp chứng chỉ
def bangcap(request):
    bangcap_data = bangcap_m.objects.order_by('stt_bc')
    form = forms.bangcap_f()

    if request.method == 'POST':
        form = forms.bangcap_f(request.POST)
        if form.is_valid():
            form.save(commit=True)
    # view pages
    page = request.GET.get('page', 1)
    paginator = Paginator(bangcap_data, 9)
    try:
        page_hienthi = paginator.page(page)
    except PageNotAnInteger:
        page_hienthi =  paginator.page(1)
    except EmptyPage:
        page_hienthi = paginator.page(paginator.num_pages)

    return render(request,'QLVB2_APP/bangcap.html',{'form':form,'bangcap_data':bangcap_data, 'page_hienthi':page_hienthi})

def taisan(request):
#     taisan_data = taisan_m.objects.order_by('-stt_ts')
#     form = forms.taisan_f()

#     if request.method == 'POST':
#         form = forms.taisan_f(request.POST)
#         if form.is_valid():
#             form.save(commit=True)

# # pages
#     page = request.GET.get('page', 1)
#     paginator = Paginator(taisan_data,5)
#     try:
#         page_hienthi = paginator.page(page)
#     except PageNotAnInteger:
#         page_hienthi =  paginator.page(1)
#     except EmptyPage:
#         page_hienthi = paginator.page(paginator.num_pages)
#     return render(request,'QLVB2_APP/taisan.html',
#                  {'form':form,'taisan_data':taisan_data, 'page_hienthi':page_hienthi})
    return render(request,'QLVB2_APP/taisan.html')


@login_required(login_url='QLVB2_APP:login')
def congtacchuyenmon(request):
    danhmuc_congtacchuyenmon = themmoi_m.objects.order_by('-stt_name')[:10]
    return render(request,'QLVB2_APP/congtacchuyenmon.html', context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon})


# @login_required(login_url='QLVB2_APP:login')
def tongsocongviec(request):
    danhmuc_congtacchuyenmon = themmoi_m.objects.order_by('-stt_name').order_by('-stt_name')
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    return render(request, 'QLVB2_APP/tongsocongviec.html', context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                                                                    'Myfilter':Myfilter})

# @login_required(login_url='QLVB2_APP:login')
def hoanthanh(request):
    danhmuc_congtacchuyenmon = themmoi_m.objects.filter(tiendo_name='2').order_by('-stt_name')
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    return render(request, 'QLVB2_APP/hoanthanh.html',context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                                                               'Myfilter':Myfilter})

# @login_required(login_url='QLVB2_APP:login')
def dangthuchien(request):
    danhmuc_congtacchuyenmon = dangthuchien = themmoi_m.objects.filter(tiendo_name='1').order_by('-stt_name')
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(danhmuc_congtacchuyenmon, 5)
    try:
        page_hienthi = paginator.page(page)
    except PageNotAnInteger:
        page_hienthi =  paginator.page(1)
    except EmptyPage:
        page_hienthi = paginator.page(paginator.num_pages)


    return render(request, 'QLVB2_APP/dangthuchien.html',context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                                                                  'Myfilter':Myfilter, 'page_hienthi':page_hienthi})

# @login_required(login_url='QLVB2_APP:login')
def chamtiendo(request):
    danhmuc_congtacchuyenmon = themmoi_m.objects.filter(tiendo_name='3').order_by('-stt_name')
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    return render(request, 'QLVB2_APP/chamtiendo.html',context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                                                                'Myfilter':Myfilter})

def giahan(request):
    danhmuc_congtacchuyenmon = themmoi_m.objects.filter(tiendo_name='4').order_by('-stt_name')
    Myfilter = tongsofilter(request.GET, queryset=danhmuc_congtacchuyenmon)
    danhmuc_congtacchuyenmon = Myfilter.qs
    return render(request, 'QLVB2_APP/chamtiendo.html',context={'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                                                                'Myfilter':Myfilter})


# @login_required(login_url='QLVB2_APP:login')
def lienhe(request):
    return render(request, 'QLVB2_APP/lienhe.html')


@login_required(login_url='QLVB2_APP:login')
def nhapdulieu_chuyenmon(request):
    danhmuc_congtacchuyenmon = themmoi_m.objects.filter(tiendo_name='3').order_by('-stt_name')[:7]
    tiendo_data = tiendo.objects.all()
    thuchien_data = thuchien_m.objects.all()
    form = forms.themmoi_f()

    if request.method == 'POST':
        form = forms.themmoi_f(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'QLVB2_APP/nhapdulieuchuyenmon.html',
                 {'form':form,'congtacchuyenmon_record':danhmuc_congtacchuyenmon,
                 'tiendo_data': tiendo_data,'thuchien_data':thuchien_data})

def dulieubaocaotuan(request):
    dulieubaocaotuan = bctuan_m.objects.order_by('-stt_bct')
    form = forms.bctuan_f()

    if request.method == 'POST':
        form = forms.bctuan_f(request.POST)
        if form.is_valid():
            form.save(commit=True)
# pages
    page = request.GET.get('page', 1)
    paginator = Paginator(dulieubaocaotuan,10)
    try:
        page_hienthi = paginator.page(page)
    except PageNotAnInteger:
        page_hienthi =  paginator.page(1)
    except EmptyPage:
        page_hienthi = paginator.page(paginator.num_pages)
    return render(request,'QLVB2_APP/dulieubaocaotuan.html',
                 {'form':form,'dulieubaocaotuan':dulieubaocaotuan, 'page_hienthi':page_hienthi })

@login_required(login_url='QLVB2_APP:login')
def edit_dulieu(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)
        context = {'form': form}
        return render(request, 'QLVB2_APP/edit_congviec.html', context)


@login_required(login_url='QLVB2_APP:login')
def edit_congviec(request, pk):
    return edit_dulieu(request, pk, themmoi_m, forms.themmoi_f)

@login_required(login_url='QLVB2_APP:login')
def edit_taisan(request, pk):
    return edit_dulieu(request, pk, taisan_m, forms.taisan_f)

@login_required(login_url='QLVB2_APP:login')
def edit_bangcap(request, pk):
    return edit_dulieu(request, pk, bangcap_m, forms.bangcap_f)

def edit_bctuan(request, pk):
    return edit_dulieu(request, pk, bctuan_m, forms.bctuan_f)

@login_required(login_url='QLVB2_APP:login')
def delete_congviec(request, pk):
	delete_congviec = themmoi_m.objects.get(stt_name=pk)
	if request.method == "POST":
		delete_congviec.delete()
		return redirect('index')

	context = {'delete_congviec':delete_congviec}
	return render(request, 'QLVB2_APP/delete.html', context)

@login_required(login_url='QLVB2_APP:login')
def delete_taisan(request, pk):
	delete_taisan = taisan_m.objects.get(stt_ts=pk)
	if request.method == "POST":
		delete_taisan.delete()
		return redirect('QLVB2_APP:taisan')

	context = {'delete_taisan':delete_taisan}
	return render(request, 'QLVB2_APP/delete_TS.html', context)

@login_required(login_url='QLVB2_APP:login')
def delete_bangcap(request, pk):
	delete_bangcap = bangcap_m.objects.get(stt_bc=pk)
	if request.method == "POST":
		delete_bangcap.delete()
		return redirect('QLVB2_APP:bangcap')

	context = {'delete_bangcap':delete_bangcap}
	return render(request, 'QLVB2_APP/delete_BC.html', context)

@login_required(login_url='QLVB2_APP:login')
def upload(request):
    listfile_duongdan = duongdan_m.objects.all().order_by('-id')
    if request.method =="POST":
        form = forms.uploadform_f(request.POST, request.FILES)
        if form.is_valid():
            form.nguoiupload = request.user.last_name
            form.save(commit=True)
            # print(UploadFile.name)
            return redirect('QLVB2_APP:upload')
    else:
        form = forms.uploadform_f()
    # view pages
    page = request.GET.get('page', 1)
    paginator = Paginator(listfile_duongdan, 12)
    try:
        page_hienthi = paginator.page(page)
    except PageNotAnInteger:
        page_hienthi =  paginator.page(1)
    except EmptyPage:
        page_hienthi = paginator.page(paginator.num_pages)
    return render(request, 'QLVB2_APP/upload.html', {'form':form, 'listfile_duongdan': listfile_duongdan, 'page_hienthi':page_hienthi})
