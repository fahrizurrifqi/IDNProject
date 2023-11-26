from django import forms
from .models import *

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('nama_training','harga','lokasi','keterangan')


class PermintaanForm(forms.ModelForm):
    class Meta:
        model = Permintaan
        fields = ('nama_client','alamat','perusahaan','no_hp','email','jumlah_permintaan')


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ('Nama','Perusahaan','Email','file')


class PenawaranForm(forms.ModelForm):
    class Meta:
        model = Penawaran
        fields = ('nama_client','training','Lokasi')

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('Nama_Client','Training','Jumlah')
