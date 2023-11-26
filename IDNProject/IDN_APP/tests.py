from django.test import TestCase

# Create your tests here.
from os import chdir, getcwd, listdir, path
from time import strftime
from win32com import client

def create_pdf():
    folder = "C:\\Users\\diqad\\Documents\\Skripsi\\IDNProject\\IDN_APP\\static\\penawaran"
    word = client.DispatchEx("Word.Application")
    files = 'Tammy Johnson.docx'
    new_name = files.replace(".docx", r".pdf")
    in_file = path.abspath(folder + "\\" + files)
    new_file = path.abspath(folder + "\\" + new_name)
    doc = word.Documents.Open(in_file)
    doc.SaveAs(new_file, FileFormat = 17)
    doc.Close()
    word.Quit()
