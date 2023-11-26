from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from mailmerge import MailMerge
from datetime import date
import os
import sys
import re
from django.conf import settings
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import locale
from os import chdir, getcwd, listdir, path
import win32com.client as win32
from pywintypes import com_error
import pythoncom
from django.db.models import Q

def rupiah_format(angka, with_prefix=False, desimal=0):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format_string("%.*f", (desimal, angka), True)
    return rupiah


# Create your views here.
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class ChartDataPN(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		#articles = dict()
		#articles['January'] = 10
		#for company in Company.objects.all():
		#    if company.articles > 0:
		#        articles[company.name] = company.articles
		#articles = sorted(articles.items(), key=lambda x: x[1])
		#articles = dict(articles)
		a = Penawaran.objects.filter(tanggal__month='01').count()
		b = Penawaran.objects.filter(tanggal__month='02').count()
		c = Penawaran.objects.filter(tanggal__month='03').count()
		d = Penawaran.objects.filter(tanggal__month='04').count()
		e = Penawaran.objects.filter(tanggal__month='05').count()
		f = Penawaran.objects.filter(tanggal__month='06').count()
		g = Penawaran.objects.filter(tanggal__month='07').count()
		h = Penawaran.objects.filter(tanggal__month='08').count()
		i = Penawaran.objects.filter(tanggal__month='09').count()
		j = Penawaran.objects.filter(tanggal__month='10').count()
		k = Penawaran.objects.filter(tanggal__month='11').count()
		l = Penawaran.objects.filter(tanggal__month='12').count()
		m = Invoice.objects.filter(tgl_inv__month='01').count()
		n = Invoice.objects.filter(tgl_inv__month='02').count()
		o = Invoice.objects.filter(tgl_inv__month='03').count()
		p = Invoice.objects.filter(tgl_inv__month='04').count()
		q = Invoice.objects.filter(tgl_inv__month='05').count()
		r = Invoice.objects.filter(tgl_inv__month='06').count()
		s = Invoice.objects.filter(tgl_inv__month='07').count()
		t = Invoice.objects.filter(tgl_inv__month='08').count()
		u = Invoice.objects.filter(tgl_inv__month='09').count()
		v = Invoice.objects.filter(tgl_inv__month='10').count()
		w = Invoice.objects.filter(tgl_inv__month='11').count()
		x = Invoice.objects.filter(tgl_inv__month='12').count()
		data = {
		"article_labels": ["Januari","Februari","Maret",'April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],#articles.keys(),
		"article_data_penawaran": [a,b,c,d,e,f,g,h,i,j,k,l],#articles.values(),
		"article_data_invoice": [m,n,o,p,q,r,s,t,u,v,w,x],
		}
		test1 = go.Bar(x=data["article_labels"],y=data['article_data_penawaran'],name='penawaran',marker={'color':'#1FC2F3'})
		test2 = go.Bar(x=data["article_labels"],y=data['article_data_invoice'],name='invoice',marker={'color':'#F31F1F'})
		test = [test1,test2]
		layout = go.Layout(title='Report Monthly')
		fig = go.Figure(data=test,layout=layout)

		pyo.plot(fig, filename='IDN_APP\\templates\\hasil.html', auto_open=False)
		return redirect('display_penawaran')

class ChartDataINV(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		#articles = dict()
		#articles['January'] = 10
		#for company in Company.objects.all():
		#    if company.articles > 0:
		#        articles[company.name] = company.articles
		#articles = sorted(articles.items(), key=lambda x: x[1])
		#articles = dict(articles)
		a = Penawaran.objects.filter(tanggal__month='01').count()
		b = Penawaran.objects.filter(tanggal__month='02').count()
		c = Penawaran.objects.filter(tanggal__month='03').count()
		d = Penawaran.objects.filter(tanggal__month='04').count()
		e = Penawaran.objects.filter(tanggal__month='05').count()
		f = Penawaran.objects.filter(tanggal__month='06').count()
		g = Penawaran.objects.filter(tanggal__month='07').count()
		h = Penawaran.objects.filter(tanggal__month='08').count()
		i = Penawaran.objects.filter(tanggal__month='09').count()
		j = Penawaran.objects.filter(tanggal__month='10').count()
		k = Penawaran.objects.filter(tanggal__month='11').count()
		l = Penawaran.objects.filter(tanggal__month='12').count()
		m = Invoice.objects.filter(tgl_inv__month='01').count()
		n = Invoice.objects.filter(tgl_inv__month='02').count()
		o = Invoice.objects.filter(tgl_inv__month='03').count()
		p = Invoice.objects.filter(tgl_inv__month='04').count()
		q = Invoice.objects.filter(tgl_inv__month='05').count()
		r = Invoice.objects.filter(tgl_inv__month='06').count()
		s = Invoice.objects.filter(tgl_inv__month='07').count()
		t = Invoice.objects.filter(tgl_inv__month='08').count()
		u = Invoice.objects.filter(tgl_inv__month='09').count()
		v = Invoice.objects.filter(tgl_inv__month='10').count()
		w = Invoice.objects.filter(tgl_inv__month='11').count()
		x = Invoice.objects.filter(tgl_inv__month='12').count()
		data = {
		"article_labels": ["Januari","Februari","Maret",'April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'],#articles.keys(),
		"article_data_penawaran": [a,b,c,d,e,f,g,h,i,j,k,l],#articles.values(),
		"article_data_invoice": [m,n,o,p,q,r,s,t,u,v,w,x],
		}
		test1 = go.Bar(x=data["article_labels"],y=data['article_data_penawaran'],name='penawaran',marker={'color':'#acacac'})
		test2 = go.Bar(x=data["article_labels"],y=data['article_data_invoice'],name='invoice',marker={'color':'#ededed'})
		test = [test1,test2]
		layout = go.Layout(title='Report Monthly')
		fig = go.Figure(data=test,layout=layout)

		pyo.plot(fig, filename='IDN_APP\\templates\\hasil.html', auto_open=False)
		return redirect('display_invoice')

@login_required
def display_laporan(request):
	return render(request, 'hasil.html', {})


def index(request):
    #return render(request, 'index.html')
    return render(request, 'login.html')

@login_required
def display_training(request):
    trainings = Training.objects.all()
    context = {'trainings':trainings,'header':'Training'}
    return render(request, 'training.html', context)

@login_required
def display_permintaan(request):
    permintaans = Permintaan.objects.all()
    context = {'permintaans':permintaans,'header':'Permintaan'}
    return render(request, 'permintaan.html', context)

@login_required
def display_po(request):
    pos = PurchaseOrder.objects.all()
    context = {'pos':pos}
    return render(request, 'po.html', context)

@login_required
def display_penawaran(request):
    penawarans = Penawaran.objects.all()
    context = {'penawarans':penawarans,'header':'Penawaran'}
    return render(request, 'penawaran.html', context)

@login_required
def display_invoice(request):
    invoices = Invoice.objects.all()
    context = {'invoices':invoices,'header':'Invoice'}
    return render(request, 'invoice.html', context)

@login_required
def add_training(request):
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_training')

    else:
        form = TrainingForm()
        return render(request, 'add_training.html', {'form':form})

@login_required
def add_permintaan(request):
    if request.method == "POST":
        form = PermintaanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_permintaan')

    else:
        form = PermintaanForm()
        return render(request, 'add_permintaan.html', {'form':form})


@login_required
def add_po(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            form.save()
            return redirect('display_po')

    else:
        form = PurchaseOrderForm()
        return render(request, 'add_po.html', {'form':form})

@login_required
def add_penawaran(request):
    if request.method == "POST":
        form = PenawaranForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_penawaran')
        return HttpResponse('form tidak valid')

    else:
        form = PenawaranForm()
        return render(request, 'add_penawaran.html', {'form':form})

@login_required
def add_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_invoice')

    else:
        form = InvoiceForm()
        return render(request, 'add_invoice.html', {'form':form})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                permintaans = Permintaan.objects.all()
                context = {'permintaans':permintaans,'header':'Permintaan'}
                return render(request, 'permintaan.html', context)
            else:
                return HttpResponse("Account not active.")
        else:
            # If account is not active:
            return HttpResponse("Invalid login.")
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def edit_training(request, pk):
    item = get_object_or_404(Training, pk=pk)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_training')

    else:
        form = TrainingForm(instance=item)
        return render(request, "edit_training.html", {"form":form})

@login_required
def edit_permintaan(request, pk):
    item = get_object_or_404(Permintaan, pk=pk)
    if request.method == "POST":
        form = PermintaanForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_permintaan')

    else:
        form = PermintaanForm(instance=item)
        return render(request, "edit_permintaan.html", {"form":form})

@login_required
def edit_po(request, pk):
    item = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_po')

    else:
        form = PurchaseOrderForm(instance=item)
        return render(request, "edit_po.html", {"form":form})

@login_required
def edit_penawaran(request, pk):
    item = get_object_or_404(Penawaran, pk=pk)
    if request.method == "POST":
        form = PenawaranForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_penawaran')

    else:
        form = PenawaranForm(instance=item)
        return render(request, "edit_penawaran.html", {"form":form})

@login_required
def edit_invoice(request, pk):
    item = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_invoice')

    else:
        form = InvoiceForm(instance=item)
        return render(request, "edit_invoice.html", {"form":form})

@login_required
def delete_training(request,pk=None):
    object = Training.objects.get(pk=pk)
    object.delete()
    return redirect('display_training')

@login_required
def delete_permintaan(request,pk=None):
    object = Permintaan.objects.get(pk=pk)
    object.delete()
    return redirect('display_permintaan')

@login_required
def delete_po(request,pk=None):
    object = PurchaseOrder.objects.get(pk=pk)
    object.delete()
    return redirect('display_po')

@login_required
def delete_penawaran(request,pk=None):
    object = Penawaran.objects.get(pk=pk)
    object.delete()
    return redirect('display_penawaran')

@login_required
def delete_invoice(request,pk=None):
    object = Invoice.objects.get(pk=pk)
    object.delete()
    return redirect('display_invoice')

def generate_penawaran(request,pk=None):
    template = os.path.join(THIS_FOLDER, 'penawaran.docx')
    #folder_hasil = os.path.join(THIS_FOLDER, 'penawaran')
    document = MailMerge(template)
    object = Penawaran.objects.filter(pk=pk)
    filepath = os.path.join(THIS_FOLDER, 'static', 'penawaran/')
    for x in object:
        document.merge(
        nama =str(x.nama_client),
        no_pnw =str(x.no_pnw),
        tanggal =str(x.tanggal),
        jml_pnw =str(x.nama_client.jumlah_permintaan),
        perusahaan =str(x.nama_client.perusahaan),
        alamat =str(x.nama_client.alamat),
        harga=rupiah_format(x.training.harga),
        total = rupiah_format(x.training.harga*x.nama_client.jumlah_permintaan),
        total_harga=rupiah_format(x.training.harga*x.nama_client.jumlah_permintaan + x.training.harga*x.nama_client.jumlah_permintaan/10),
        ppn =rupiah_format(x.training.harga*x.nama_client.jumlah_permintaan/10),
        email=str(x.nama_client.email),
		lokasi=str(x.training.lokasi),
        nama_training=str(x.training))
        filename = str(x.nama_client) + '.docx'
        a = document.write(filepath+filename)
        pythoncom.CoInitialize()
        word = win32.gencache.EnsureDispatch('Word.Application')
        files = filepath+filename
        new_name = files.replace(".docx", r".pdf")
        in_file = path.abspath(files)
        new_file = path.abspath(new_name)
        doc = word.Documents.Open(in_file)
        doc.SaveAs(new_file, FileFormat = 17)
        doc.Close()
        word.Application.Quit()
    return redirect('display_penawaran')


def generate_invoice(request,pk=None):
    template = os.path.join(THIS_FOLDER, 'invoice1.docx')
    #folder_hasil = os.path.join(THIS_FOLDER, 'penawaran')
    document = MailMerge(template)
    object = Invoice.objects.filter(pk=pk)
    filepath = os.path.join(THIS_FOLDER, 'static', 'invoice/')
    for x in object:
        document.merge(
		email = str(x.Nama_Client.Email),
        nama =str(x.Nama_Client),
        inv_no =str(x.no_inv),
        tanggal =str(x.tgl_inv),
        jumlah =str(x.Jumlah),
        perusahaan =str(x.Nama_Client.Perusahaan),
        harga=rupiah_format(x.Training.harga),
        totals=rupiah_format(x.Training.harga*x.Jumlah),
        training=str(x.Training),
		total_harga = rupiah_format(x.Training.harga*x.Jumlah+x.Training.harga*x.Jumlah/10),
		ppn = rupiah_format(x.Training.harga*x.Jumlah/10))
        filename = str(x.Nama_Client) + '.docx'
        a = document.write(filepath+filename)
        pythoncom.CoInitialize()
        word = win32.gencache.EnsureDispatch('Word.Application')
        files = filepath+filename
        new_name = files.replace(".docx", r".pdf")
        in_file = path.abspath(files)
        new_file = path.abspath(new_name)
        doc = word.Documents.Open(in_file)
        doc.SaveAs(new_file, FileFormat = 17)
        doc.Close()
        word.Application.Quit()
    return redirect('display_invoice')
