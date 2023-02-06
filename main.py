import sys
from tkinter.messagebox import YES
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from admin_ekle import *

uygulama=QApplication(sys.argv)
pencere=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()
ui.aramapanel.hide()

import sqlite3
baglanti=sqlite3.connect("kullanici.db")
islem=baglanti.cursor()
baglanti.commit()

table=islem.execute("create table if not exists admin(kullanici text, sifre text,yetki text)")
baglanti.commit()

def admin_ekle():
    kul=ui.kultxt.text()
    sifre=ui.sifretxt.text()
    yetki=ui.yetkicmb.currentText()
    try:
        cumle="insert into admin (kullanici, sifre,yetki) values (?,?,?)";
        islem.execute(cumle,(kul,sifre,yetki))
        baglanti.commit()
        ui.statusbar.showMessage("Kaydınız Başarılı Şekilde Yapıldı",5000)
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Ekleme Hatası"+str(error))
    
def kayit_listeleme():
    ui.tablom.clear()
    ui.tablom.setHorizontalHeaderLabels(("Kullanıcı Adı","Şifre","Yetki"))
    ui.tablom.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu="select * from admin"
    islem.execute(sorgu)
    for indexsatir, kayitnumarasi in enumerate(islem):
        for indexsutun, kayitsutun in enumerate(kayitnumarasi):
            ui.tablom.setItem(indexsatir,indexsutun,QTableWidgetItem(str(kayitsutun)))
def kayit_guncelleme():
        sil_mesaj=QMessageBox.question(pencere,"Güncelleme Onayı","Güncelleme İstediğiniz Emin misiniz?",QMessageBox.Yes|QMessageBox.No)
        if sil_mesaj==QMessageBox.Yes:
            

def kayit_bul():
    ui.tablom.clear()
    aranan=ui.arayicitxt.text()
    sorgu="Select * from kullanici where kullanici==?"
    try:
        islem.execute(sorgu,aranan)
        baglanti.commit()
    
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Bulma Hatası"+str(error))

def gosterme(self):
        ui.aramapanel.show()

def kayit_sil():
    sil_mesaj=QMessageBox.question(pencere,"Silme Onayı","Silmek İstediğiniz Emin misiniz?",QMessageBox.Yes|QMessageBox.No)
    if sil_mesaj==QMessageBox.Yes:
        secilen_kayit=ui.arayicitxt.text()
        sorgu="Delete from admin where kullanici==?"

        try:
            islem.execute(sorgu,secilen_kayit)
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Silindi",5000)
        
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Silinmedi"+str(error))






ui.eklebtn.clicked.connect(admin_ekle)
ui.listelebtn.clicked.connect(kayit_listeleme)
ui.aramabtn.clicked.connect(gosterme)
ui.silmebtn.clicked.connect(kayit_sil)

sys.exit(uygulama.exec_())
