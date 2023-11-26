from django.urls import re_path
from .views import *
from django.urls import path

urlpatterns =[
    re_path(r'^user_login/$',user_login,name='user_login'),
    re_path(r'^user_logout/$', user_logout,name='user_logout'),
    re_path(r'^$', index, name='index'),
    re_path(r'^display_training$', display_training, name='display_training'),
    re_path(r'^display_permintaan$', display_permintaan, name='display_permintaan'),
    re_path(r'^display_po$', display_po, name='display_po'),
    re_path(r'^display_penawaran$', display_penawaran, name='display_penawaran'),
    re_path(r'^display_invoice$', display_invoice, name='display_invoice'),
    re_path(r'^add_training$', add_training, name="add_training"),
    re_path(r'^add_permintaan$', add_permintaan, name="add_permintaan"),
    re_path(r'^add_po$', add_po, name="add_po"),
    re_path(r'^add_penawaran$', add_penawaran, name="add_penawaran"),
    re_path(r'^add_invoice$', add_invoice, name="add_invoice"),
    re_path(r'^edit_training/(?P<pk>\d+)$', edit_training, name="edit_training"),
    re_path(r'^edit_permintaan/(?P<pk>\d+)$', edit_permintaan, name="edit_permintaan"),
    re_path(r'^edit_po/(?P<pk>\d+)$', edit_po, name="edit_po"),
    re_path(r'^edit_penawaran/(?P<pk>\d+)$', edit_penawaran, name="edit_penawaran"),
    re_path(r'^edit_invoice/(?P<pk>\d+)$', edit_invoice, name="edit_invoice"),
    re_path(r'^delete_training/(?P<pk>\d+)$', delete_training, name="delete_training"),
    re_path(r'^delete_permintaan/(?P<pk>\d+)$', delete_permintaan, name="delete_permintaan"),
    re_path(r'^delete_po/(?P<pk>\d+)$', delete_po, name="delete_po"),
    re_path(r'^delete_penawaran/(?P<pk>\d+)$', delete_penawaran, name="delete_penawaran"),
    re_path(r'^delete_invoice/(?P<pk>\d+)$', delete_invoice, name="delete_invoice"),
    re_path(r'^generate_penawaran/(?P<pk>\d+)$', generate_penawaran, name="generate_penawaran"),
    re_path(r'^generate_invoice/(?P<pk>\d+)$', generate_invoice, name="generate_invoice"),
    re_path(r'^display_laporan$', display_laporan, name="display_laporan"),
    re_path(r'^update_laporan_pn$', ChartDataPN.as_view(), name='update_laporan_pn'),
    re_path(r'^update_laporan_inv$', ChartDataINV.as_view(), name='update_laporan_inv'),

]
