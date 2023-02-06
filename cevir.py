from PyQt5 import uic

with open("admin_ekle.py","w",encoding="utf-8") as fout:
    uic.compileUi("pencere.ui",fout)