#PEMBELIAN MERCHANT
import mysql.connector
import os
import random as rd


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pembelian_merchant"
)

if db.is_connected():
    print("Berhasil terhubung ke database")

merchant=dict(
    pilihan="", 
    pilihangroup="",
    posisi="",
    jumlah= 0,
    harga=0,
    totalharga=0,
)
def pembatas():
    print("-"*110)
def pembatas2():
    print("="*46)
def pembatas3():
    print("-"*73)
def pembatas4():
    print("-"*90)

#1.1_Pilihan Group
def daftarboygirl():
        pembatas()
        print(" DAFTAR BOY & GIRLGROUP ".center(110, "-"))
        pembatas()
        print("1. NCT Dream")
        print("2. NCT 127")
        print("3. WAYV")
        print("4. EXO")
        print("5. SHINee")
        print("6. Red Velvet")
        print("7. Aespa")
        print("0. Kembali")

def NCT_Dream():
    os.system("cls")
    print("\n")
    pembatas()
    print(" Group NCT Dream ".center(110, "*"))
    pembatas()
    nctdrm=dict(harga1=105000, harga2=660000, harga3=165000, harga4=295000, harga5=234000, harga6=700000, harga7=180000, 
                harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                                        |", nctdrm.get("harga1"), "|        ")
    print("2. Lightstick                                                 |", nctdrm.get("harga2"), "|        ")
    print("3. Danji Key Ring                                             |", nctdrm.get("harga3"), "|        ")
    print("4. Winter Special Mini Album [Candy] (Photobook Ver.)         |", nctdrm.get("harga4"), "|        ")
    print("5. Winter Special Mini Album [Candy] (Digipack Ver.)          |", nctdrm.get("harga5"), "|        ")
    print("6. Mood Lamp                                                  |", nctdrm.get("harga6"), "|        ")
    print("7. Cup                                                        |", nctdrm.get("harga7"), "|        ")
    print("8. Sticker                                                    |", nctdrm.get("harga8"), " |        ")
    print("9. Sling Bag                                                  |", nctdrm.get("harga9"), "|        ")
    print("10. T-Shirt                                                   |", nctdrm.get("harga10"), "|        ")
    print("11. Tumbler                                                   |", nctdrm.get("harga11"), "|        ")
    print("12. Hat                                                       |", nctdrm.get("harga12"), "|        ")
    print("13. Pop Socket                                                |", nctdrm.get("harga13"), "|        ")
    print("14. Casing                                                    |", nctdrm.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", nctdrm.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==2:
        print("Lightstick dengan harga", nctdrm.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Danji Key Ring dengan harga", nctdrm.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga3")
        print("Danji Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("Winter Special Mini Album [Candy] (Photobook Ver.) dengan harga", nctdrm.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga4")
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("Winter Special Mini Album [Candy] (Digipack Ver.) dengan harga", nctdrm.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga5")
        print("Winter Special Mini Album [Candy] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga", nctdrm.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", nctdrm.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", nctdrm.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", nctdrm.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", nctdrm.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", nctdrm.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", nctdrm.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", nctdrm.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nctdrm.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            os.system("pause")

def NCT_127():
    os.system("clc")
    print("\n")
    pembatas()
    print(" Group NCT 127".center(110, "*"))
    pembatas()
    nct127=dict(harga1=105000, harga2=660000, harga3=280000, harga4=412000, harga5=226000, harga6=700000, harga7=180000, 
                harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                 |", nct127.get("harga1"), "|        ")
    print("2. Lightstick                                                 |", nct127.get("harga2"), "|        ")
    print("3. Acrylic Stand Key Ring                                     |", nct127.get("harga3"), "|        ")
    print("4. The 4th Album [Jilju (2 Baddies)] (Photobook Ver.)         |", nct127.get("harga4"), "|        ")
    print("5. The 4th Album [Jilju (2 Baddies)] (Digipack Ver.)          |", nct127.get("harga5"), "|        ")
    print("6. Mood Lamp                                                  |", nct127.get("harga6"), "|        ")
    print("7. Cup                                                        |", nct127.get("harga7"), "|        ")
    print("8. Sticker                                                    |", nct127.get("harga8"), " |        ")
    print("9. Sling Bag                                                  |", nct127.get("harga9"), "|        ")
    print("10. T-Shirt                                                   |", nct127.get("harga10"), "|        ")
    print("11. Tumbler                                                   |", nct127.get("harga11"), "|        ")
    print("12. Hat                                                       |", nct127.get("harga12"), "|        ")
    print("13. Pop Socket                                                |", nct127.get("harga13"), "|        ")
    print("14. Casing                                                    |", nct127.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", nct127.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==2:
        print("Lightstick dengan harga", nct127.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Acrylic Stand Key Ring dengan harga", nct127.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga3")
        print("Acrylic Stand Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("The 4th Album [Jilju (2 Baddies)] (Photobook Ver.) dengan harga", nct127.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga4")
        print("The 4th Album [Jilju (2 Baddies)] (Photobook Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("The 4th Album [Jilju (2 Baddies)] (Digipack Ver.) dengan harga", nct127.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga5")
        print("The 4th Album [Jilju (2 Baddies)] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga", nct127.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", nct127.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", nct127.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", nct127.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", nct127.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", nct127.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", nct127.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", nct127.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print("Casing dengan harga", nct127.get("harga14"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * nct127("harga14")
        print("Casing", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            os.system("pause")

def WAYV():
    os.system("cls")
    print("\n")
    pembatas()
    print(" Group WAYV ".center(110, "*"))
    pembatas()
    wayv=dict(harga1=105000, harga2=700000, harga3=245000, harga4=352000, harga5=230000, harga6=700000, harga7=180000, 
                harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                 |", wayv.get("harga1"), "|        ")
    print("2. Lightstick                                                 |", wayv.get("harga2"), "|        ")
    print("3. Acrylic Key Ring                                           |", wayv.get("harga3"), "|        ")
    print("4. 4th Mini Album [Phantom] (Photobook Ver.)                  |", wayv.get("harga4"), "|        ")
    print("5. 4th Mini Album [Phantom] (Digipack Ver.)                   |", wayv.get("harga5"), "|        ")
    print("6. Mood Lamp                                                  |", wayv.get("harga6"), "|        ")
    print("7. Cup                                                        |", wayv.get("harga7"), "|        ")
    print("8. Sticker                                                    |", wayv.get("harga8"), " |        ")
    print("9. Sling Bag                                                  |", wayv.get("harga9"), "|        ")
    print("10. T-Shirt                                                   |", wayv.get("harga10"), "|        ")
    print("11. Tumbler                                                   |", wayv.get("harga11"), "|        ")
    print("12. Hat                                                       |", wayv.get("harga12"), "|        ")
    print("13. Pop Socket                                                |", wayv.get("harga13"), "|        ")
    print("14. Casing                                                    |", wayv.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", wayv.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    if pilihan==2:
        print("Lightstick dengan harga", wayv.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Acrylic Key Ring dengan harga", wayv.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga3")
        print("Acrylic Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("4th Mini Album [Phantom] (Photobook Ver.) dengan harga", wayv.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga4")
        print("4th Mini Album [Phantom] (Photobook Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("4th Mini Album [Phantom] (Digipack Ver.) dengan harga", wayv.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga5")
        print("4th Mini Album [Phantom] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga", wayv.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", wayv.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", wayv.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", wayv.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", wayv.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", wayv.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", wayv.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", wayv.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print("Casing dengan harga", wayv.get("harga14"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * wayv.get("harga14")
        print("Casing", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            os.system("pause")

def EXO():
    os.system("cls")
    print("\n")
    pembatas()
    print(" Group EXO ".center(110, "*"))
    pembatas()
    exo=dict(harga1=105000, harga2=580000, harga3=300000, harga4=379000, harga5=264000, harga6=700000, harga7=180000, 
                harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                 |", exo.get("harga1"), "|        ")
    print("2. Lightstick                                                 |", exo.get("harga2"), "|        ")
    print("3. Voice Key Ring                                             |", exo.get("harga3"), "|        ")
    print("4. Special Album [Don't Fight The Feeling] (Photobook Ver.)   |", exo.get("harga4"), "|        ")
    print("5. 2nd Mini Album [Grey Suit] (Digipack Ver.)                 |", exo.get("harga5"), "|        ")
    print("6. Mood Lamp                                                  |", exo.get("harga6"), "|        ")
    print("7. Cup                                                        |", exo.get("harga7"), "|        ")
    print("8. Sticker                                                    |", exo.get("harga8"), " |        ")
    print("9. Sling Bag                                                  |", exo.get("harga9"), "|        ")
    print("10. T-Shirt                                                   |", exo.get("harga10"), "|        ")
    print("11. Tumbler                                                   |", exo.get("harga11"), "|        ")
    print("12. Hat                                                       |", exo.get("harga12"), "|        ")
    print("13. Pop Socket                                                |", exo.get("harga13"), "|        ")
    print("14. Casing                                                    |", exo.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", exo.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==2:
        print("Lightstick dengan harga", exo.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Voice Key Ring dengan harga", exo.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga3")
        print("Voice Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("Special Album [Don't Fight The Feeling] (Photobook Ver.) dengan harga", exo.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga4")
        print("Special Album [Don't Fight The Feeling] (Photobook Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("2nd Mini Album - Suho [Grey Suit] (Digipack Ver.) dengan harga", exo.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga5")
        print("2nd Mini Album - Suho [Grey Suit] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga", exo.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", exo.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", exo.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", exo.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", exo.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", exo.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", exo.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", exo.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print("Casing dengan harga", exo.get("harga14"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * exo.get("harga14")
        print("Casing", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            os.system("pause")

def SHINee():
    os.system("cls")
    print("\n")
    pembatas()
    print(" Group SHINee ".center(73, "*"))
    pembatas4()
    shinee=dict(harga1=105000, harga2=585000, harga3=150000, harga4=332000, harga5=230000, harga6=700000, harga7=180000, 
                harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                 |", shinee.get("harga1"), "|        ")
    print("2. Lightstick                                                 |", shinee.get("harga2"), "|        ")
    print("3. Acrylic Key Ring                                           |", shinee.get("harga3"), "|        ")
    print("4. 7th Album [Don't Call Me] (Photobook Ver.)                 |", shinee.get("harga4"), "|        ")
    print("5. 2nd Mini Album [Dice] (Digipack Ver.)                      |", shinee.get("harga5"), "|        ")
    print("6. Mood Lamp                                                  |", shinee.get("harga6"), "|        ")
    print("7. Cup                                                        |", shinee.get("harga7"), "|        ")
    print("8. Sticker                                                    |", shinee.get("harga8"), " |        ")
    print("9. Sling Bag                                                  |", shinee.get("harga9"), "|        ")
    print("10. T-Shirt                                                   |", shinee.get("harga10"), "|        ")
    print("11. Tumbler                                                   |", shinee.get("harga11"), "|        ")
    print("12. Hat                                                       |", shinee.get("harga12"), "|        ")
    print("13. Pop Socket                                                |", shinee.get("harga13"), "|        ")
    print("14. Casing                                                    |", shinee.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", shinee.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==2:
        print("Lightstick dengan harga", shinee.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Acrylic Key Ring dengan harga", shinee.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga3")
        print("Acrylic Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("7th Album [Don't Call Me] (Photobook Ver.) dengan harga", shinee.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga4")
        print("7th Album [Don't Call Me] (Photobook Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("2nd Mini Album [Dice] (Digipack Ver.) dengan harga", shinee.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga5")
        print("2nd Mini Album [Dice] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga",shinee.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", shinee.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", shinee.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", shinee.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", shinee.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", shinee.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", shinee.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", shinee.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print("Casing dengan harga", shinee.get("harga14"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * shinee.get("harga14")
        print("Casing", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            os.system("pause")

def RedVelvet():
    os.system("cls")
    print("\n")
    pembatas()
    print(" Group Red Velvet".center(110, "*"))
    pembatas()
    redve=dict(harga1=105000, harga2=615000, harga3=160000, harga4=428000, harga5=253000, harga6=700000, harga7=180000, 
                harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                                        |", redve.get("harga1"), "|        ")
    print("2. Lightstick                                                                        |", redve.get("harga2"), "|        ")
    print("3. Acrylic Key Ring                                                                  |", redve.get("harga3"), "|        ")
    print("4. Mini Album [The ReVe Festival 2022 : Feel My Rhythm] (Photobook Ver.)             |", redve.get("harga4"), "|        ")
    print("5. Mini Album [The ReVe Festival 2022 : Birthday] (Digipack Ver.)                    |", redve.get("harga5"), "|        ")
    print("6. Mood Lamp                                                                         |", redve.get("harga6"), "|        ")
    print("7. Cup                                                                               |", redve.get("harga7"), "|        ")
    print("8. Sticker                                                                           |", redve.get("harga8"), " |        ")
    print("9. Sling Bag                                                                         |", redve.get("harga9"), "|        ")
    print("10. T-Shirt                                                                          |", redve.get("harga10"), "|        ")
    print("11. Tumbler                                                                          |", redve.get("harga11"), "|        ")
    print("12. Hat                                                                              |", redve.get("harga12"), "|        ")
    print("13. Pop Socket                                                                       |", redve.get("harga13"), "|        ")
    print("14. Casing                                                                           |", redve.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", redve.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==2:
        print("Lightstick dengan harga", redve.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Acrylic Key Ring dengan harga", redve.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga3")
        print("Acrylic Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("Mini Album [The ReVe Festival 2022 : Feel My Rhythm] (Photobook Ver.) dengan harga", redve.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga4")
        print("Mini Album [The ReVe Festival 2022 : Feel My Rhythm] (Photobook Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("Mini Album [The ReVe Festival 2022 : Birthday] (Digipack Ver.) dengan harga", redve.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga5")
        print("Mini Album [The ReVe Festival 2022 : Birthday] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga",redve.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", redve.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", redve.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", redve.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", redve.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", redve.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", redve.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", redve.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print("Casing dengan harga", redve.get("harga14"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * redve.get("harga14")
        print("Casing", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            os.system("pause")

def Aespa():
    os.system("cls")
    print("\n")
    pembatas()
    print(" Group Aespa ".center(110, "*"))
    pembatas()
    aespa=dict(harga1=105000, harga2=649000, harga3=250000, harga4=330000, harga5=256000, harga6=700000, harga7=180000, harga8=95000,
               harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
    print("1. 4x6 Photo + Photo Card Set                                 |", aespa.get("harga1"), "|        ")
    print("2. Lightstick                                                 |", aespa.get("harga2"), "|        ")
    print("3. Acrylic Stand Key Ring                                     |", aespa.get("harga3"), "|        ")
    print("4. 2nd Mini Album [Girls] (Photobook Ver.)                    |", aespa.get("harga4"), "|        ")
    print("5. 2nd Mini Album [Girls] (Digipack Ver.)                     |", aespa.get("harga5"), "|        ")
    print("6. Mood Lamp                                                  |", aespa.get("harga6"), "|        ")
    print("7. Cup                                                        |", aespa.get("harga7"), "|        ")
    print("8. Sticker                                                    |", aespa.get("harga8"), " |        ")
    print("9. Sling Bag                                                  |", aespa.get("harga9"), "|        ")
    print("10. T-Shirt                                                   |", aespa.get("harga10"), "|        ")
    print("11. Tumbler                                                   |", aespa.get("harga11"), "|        ")
    print("12. Hat                                                       |", aespa.get("harga12"), "|        ")
    print("13. Pop Socket                                                |", aespa.get("harga13"), "|        ")
    print("14. Casing                                                    |", aespa.get("harga14"), "|        ")
    pilihan=int(input("\nMau beli product apa [1/2]?: "))
    merchant['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("4x6 Photo + Photo Card Set dengan harga", aespa.get("harga1"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga1")
        print("4x6 Photo + Photo Card Set", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==2:
        print("Lightstick dengan harga", aespa.get("harga2"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga2")
        print("Lightstick", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==3:
        print("Acrylic Stand Key Ring dengan harga", aespa.get("harga3"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga3")
        print("Acrylic Key Ring", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==4:
        print("2nd Mini Album [Girls] (Photobook Ver.) dengan harga", aespa.get("harga4"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga4")
        print("2nd Mini Album [Girls] (Photobook Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==5:
        print("2nd Mini Album [Girls] (Digipack Ver.) dengan harga", aespa.get("harga5"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga5")
        print("2nd Mini Album [Girls] (Digipack Ver.)", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==6:
        print("Mood Lamp dengan harga",aespa.get("harga6"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga6")
        print("Mood Lamp", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==7:
        print("Cup dengan harga", aespa.get("harga7"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga7")
        print("Cup", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==8:
        print("Sticker dengan harga", aespa.get("harga8"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga8")
        print("Sticker", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==9:
        print("Sling Bag dengan harga", aespa.get("harga9"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga9")
        print("Sling Bag", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==10:
        print("T-Shirt dengan harga", aespa.get("harga10"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga10")
        print("T-Shirt", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==11:
        print("Tumbler dengan harga", aespa.get("harga11"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga11")
        print("Tumbler", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==12:
        print("Hat dengan harga", aespa.get("harga12"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga12")
        print("Hat", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==13:
        print("Pop Socket dengan harga", aespa.get("harga13"))
        jumlah = int(input("Beli berapa?: "))
        merchant['jumlah']=jumlah
        total_harga = merchant['jumlah'] * aespa.get("harga13")
        print("Pop Socket", "Jumlah : ", merchant.get('jumlah'),"Harga : Rp",total_harga)
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
    elif pilihan==14:
        print('\n=================================== Melakukan Pembayaran Pembelian Merchant =================================== \n')
        nama=str(input('\nMasukkan Nama Anda  : '))
        bayar=int(input('Masukkan pembayaran : ',))
        pembatas()
        merchant['bayar']=bayar
        kembalian = int(bayar-total_harga)
        merchant['total']=total_harga
        merchant['sisa']=kembalian
        #validasi 
        if total_harga>=bayar:
            print('\n================================= Pembayaran tidak memenuhi, transaksi batal =================================\n')
        else:
            print('\nHalo',nama,'!')
            print('Uang anda Rp',bayar)
            print('Kembalian anda Rp',kembalian)
            print('\n=================================== Pembayaran memenuhi, transaksi berhasil ===================================\n')
            menu_SM_store()
            os.system("pause")

#1_PEMBELIAN ALBUM 
def pembelian_merchant():
    os.system("cls")
    pembatas()
    print(" Pembelian Merchant ".center(110, "="))
    daftarboygirl()
    pilihangroup=int(input("Masukkan grup yang dipilih: "))
    if pilihangroup == 1:
        NCT_Dream()
    elif pilihangroup == 2:
        NCT_127()
    elif pilihangroup == 3:
        WAYV()
    elif pilihangroup == 4:
        EXO()
    elif pilihangroup == 5:
        SHINee()
    elif pilihangroup == 6:
        RedVelvet()
    elif pilihangroup == 7:
        Aespa()
    elif pilihangroup == 0:
        menu_SM_store()
    os.system("pause")


def tampilData():
    os.system("cls")
    cursor = db.cursor()
    print ("\n============================================================================================================")
    print ("======================================= WELCOME TO SM STORE OFFICIAL =======================================")
    print ("============================================================================================================\n")
    cursor.execute("SELECT * FROM merchant")
    hasil = cursor.fetchall()
    print("-----+----------------------------------------------------------------------------+----------------+---------+")
    print("|No  | Product                                                                    | Group          | Price   |")
    print("-----+----------------------------------------------------------------------------+----------------+---------+")
    no=0
    for x in hasil:
        no=no+1
        print("|{:3d} |".format(x[0]),
              "{:75s}|".format(x[1]),
              "{:15s}|".format(x[2]),
              "{:8d}|".format(x[3]))
    print("+----+----------------------------------------------------------------------------+----------------+---------+\n")


#MENU UTAMA FANSIGN    
def menu_SM_store():
    os.system("cls")
    pembatas()
    tampilData()
    pembatas()
    print("1. Pembelian dan Pembayaran Merchant")
    print("2. Keluar Dari SM Store Official")
    pembatas()
    pilihan= input("Pilih Menu : ")
    if pilihan == "1":
        pembelian_merchant()
    if pilihan == "2":
        pembatas()
        print('Terimakasih Telah Berbelanja Disini'.center(110, "="))
        pembatas()
        
menu_SM_store()

       
