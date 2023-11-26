from django.db import models
import datetime

# Create your models here.

class Training(models.Model):
    def number():
        no = Training.objects.count()
        if no == None:
            final = str(1)
            return final
        else:
            final = str(no + 1)
            return final
    nomor = models.CharField(max_length=20, default=number)
    nama_training = models.CharField(max_length=50,default='',blank=True)
    harga = models.IntegerField()
    lokasi = models.CharField(max_length=20)
    keterangan = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_training

class Permintaan(models.Model):
    def number():
        a = "CLI"
        x = str(datetime.datetime.now()).split("-")
        b = "IDN"
        c = x[0][2]+x[0][3]
        if x[1] == '01':
            rom = "I"
        elif x[1] == '02':
            rom = "II"
        elif x[1] == '03':
            rom = "III"
        elif x[1] == '04':
            rom = "IV"
        elif x[1] == '05':
            rom = "V"
        elif x[1] == '06':
            rom = "VI"
        elif x[1] == '07':
            rom = "VII"
        elif x[1] == '08':
            rom = "VIII"
        elif x[1] == '09':
            rom = "IX"
        elif x[1] == '10':
            rom = "X"
        elif x[1] == '11':
            rom = "XI"
        else:
            rom = "XII"
        no = Permintaan.objects.count()
        if no == None:
            final = a+"-"+str(1)+"-"+b+"-"+rom+"-"+c
            return final
        else:
            final = a+"-"+str(no + 1)+"-"+b+"-"+rom+"-"+c
            return final
    no_permintaan = models.CharField(max_length=20,default=number)
    nama_client = models.CharField(max_length=50)
    alamat = models.CharField(max_length=80,default='')
    perusahaan = models.CharField(max_length=25)
    no_hp = models.CharField(max_length=15)
    email = models.EmailField()
    jumlah_permintaan = models.IntegerField(blank=False)
    #Keterangan = models.CharField(max_length=30)
    def __str__(self):
        return self.nama_client

class PurchaseOrder(models.Model):
    def number():
        a = "PO"
        x = str(datetime.datetime.now()).split("-")
        b = "IDN"
        c = x[0][2]+x[0][3]
        if x[1] == '01':
            rom = "I"
        elif x[1] == '02':
            rom = "II"
        elif x[1] == '03':
            rom = "III"
        elif x[1] == '04':
            rom = "IV"
        elif x[1] == '05':
            rom = "V"
        elif x[1] == '06':
            rom = "VI"
        elif x[1] == '07':
            rom = "VII"
        elif x[1] == '08':
            rom = "VIII"
        elif x[1] == '09':
            rom = "IX"
        elif x[1] == '10':
            rom = "X"
        elif x[1] == '11':
            rom = "XI"
        else:
            rom = "XII"
        no = PurchaseOrder.objects.count()
        if no == None:
            final = a+"-"+str(1)+"-"+b+"-"+rom+"-"+c
            return final
        else:
            final = a+"-"+str(no + 1)+"-"+b+"-"+rom+"-"+c
            return final
    Nama = models.CharField(max_length=30)
    nomor_PO = models.CharField(max_length=20,default=number)
    tanggal = models.DateField(auto_now_add=True)
    Perusahaan = models.CharField(max_length=30)
    Email = models.EmailField()
    file = models.FileField(blank=True)
    def __str__(self):
        return self.Nama

class Penawaran(models.Model):
    def number():
        a = "PN"
        x = str(datetime.datetime.now()).split("-")
        b = "IDN"
        c = x[0][2]+x[0][3]
        if x[1] == '01':
            rom = "I"
        elif x[1] == '02':
            rom = "II"
        elif x[1] == '03':
            rom = "III"
        elif x[1] == '04':
            rom = "IV"
        elif x[1] == '05':
            rom = "V"
        elif x[1] == '06':
            rom = "VI"
        elif x[1] == '07':
            rom = "VII"
        elif x[1] == '08':
            rom = "VIII"
        elif x[1] == '09':
            rom = "IX"
        elif x[1] == '10':
            rom = "X"
        elif x[1] == '11':
            rom = "XI"
        else:
            rom = "XII"
        no = Penawaran.objects.count()
        if no == None:
            final = a+"-"+str(1)+"-"+b+"-"+rom+"-"+c
            return final
        else:
            final = a+"-"+str(no + 1)+"-"+b+"-"+rom+"-"+c
            return final

    no_pnw = models.CharField(max_length=20, default=number)
    training = models.ForeignKey(Training,on_delete=models.CASCADE,default='',blank=True)
    nama_client = models.OneToOneField(Permintaan, on_delete=models.CASCADE)
    tanggal = models.DateField(auto_now_add=True)
    #Jumlah = models.IntegerField()
    #keterangan = models.CharField(max_length=50)
    choices = (('JAKARTA', 'Jakarta'),('BODETABEK', 'Bodetabek'),('LUAR BODETABEK', 'Luar Bodetabek'))
    Lokasi = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return self.training.harga


class Invoice(models.Model):
    def number():
        a = "INV"
        x = str(datetime.datetime.now()).split("-")
        b = "IDN"
        c = x[0][2]+x[0][3]
        if x[1] == '01':
            rom = "I"
        elif x[1] == '02':
            rom = "II"
        elif x[1] == '03':
            rom = "III"
        elif x[1] == '04':
            rom = "IV"
        elif x[1] == '05':
            rom = "V"
        elif x[1] == '06':
            rom = "VI"
        elif x[1] == '07':
            rom = "VII"
        elif x[1] == '08':
            rom = "VIII"
        elif x[1] == '09':
            rom = "IX"
        elif x[1] == '10':
            rom = "X"
        elif x[1] == '11':
            rom = "XI"
        else:
            rom = "XII"
        no = Penawaran.objects.count()
        if no == None:
            final = a+"-"+str(1)+"-"+b+"-"+rom+"-"+c
            return final
        else:
            final = a+"-"+str(no + 1)+"-"+b+"-"+rom+"-"+c
            return final

    no_inv = models.CharField(max_length=20, default=number)
    #no_po = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    tgl_inv = models.DateField(auto_now_add=True)
    #KETERANGAN = models.CharField(max_length=50,blank=True)
    Nama_Client = models.OneToOneField(PurchaseOrder,on_delete=models.CASCADE)
    Training = models.ForeignKey(Training,on_delete=models.CASCADE,default='',blank=True)
    Jumlah = models.PositiveIntegerField(default='')
