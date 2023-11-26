import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','IDNProject.settings')

import django
django.setup()

import random
from IDN_APP.models import Penawaran, Permintaan, PurchaseOrder, Training, Invoice
from faker import Faker

fakegen = Faker()

angka = [1,2,3,4,5,6]
keterangan = ['belum bayar','sudah bayar']

def populate(N=5):
    for entry in range(N):
        fake_nama = fakegen.name()
        fake_alamat = fakegen.address()
        fake_perusahaan = fakegen.company()
        fake_hp = fakegen.msisdn()
        fake_email = fakegen.email()
        fake_jumlah = random.choice(angka)
        fake_keterangan = random.choice(keterangan)
        fake_date = fakegen.date()

        prmntn = Permintaan.objects.get_or_create(nama_client=fake_nama, alamat=fake_alamat,perusahaan=fake_perusahaan,
                                                no_hp=fake_hp,email=fake_email,jumlah_permintaan=fake_jumlah)[0]
        po = PurchaseOrder.objects.get_or_create(Nama=fake_nama, Perusahaan=fake_perusahaan, Email=fake_email)

if __name__ == '__main__':
    print("populating...")
    populate(20)
    print('complete')
