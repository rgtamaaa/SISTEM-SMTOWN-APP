import os
import random as rd
import datetime
now=datetime.datetime.now()
import mysql.connector

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

#dictionarylogin
inilogin=dict(
    namalengkap="", 
    namapanggilan="",
    email=""
)

#DICTIONARY PEMESANAN TIKET FANSIGN
tiket=dict(
    day="",
    group="",
    seatplan="",
    harga=0,
    jumlah=0,
    bayar=0,
)

album=dict(
    pilihan="", 
    pilihangroup="",
    posisi="",
    jumlah= 0,
    harga=0,
    totalharga=0,
)

#DICTIONARY TIKET KONSER
tiket=dict(
    day="",
    group="",
    seatplan="",
    harga=0,
    jumlah=0,
    bayar=0,
)



#pembatas
def pembatas_():
    print("-"*46)
def pembatas2_():
    print("="*46)
def pembatas3_():
    print("-"*73)
def pembatas4_():
    print("-"*90)

#Pembatas merchant
def pembatas():
    print("-"*110)
def pembatas2():
    print("="*46)
def pembatas3():
    print("-"*73)
def pembatas4():
    print("-"*90)

#PEMBATAS
def garis0():
    print('-'*69)
def garis1():
    print('='*69)
def garis2():
    print('*'*46)
def garis3():
    print('-'*46)
def garis4():
    print('='*46)

#LOGIN
def login():
    os.system("cls")
    print(" LOGIN ".center(46, "="))
    pembatas_()
    #input nama lengkap
    namalengkap = str(input("Masukkan Nama Lengkap  : "))
    inilogin['namalengkap']=namalengkap
    #input nama panggilan
    pembatas_()
    namapanggilan = str(input("Masukkan Nama Panggilan  : "))
    inilogin['namapanggilan']=namapanggilan
    #input email
    pembatas_()
    email = str(input("Masukkan Email  : "))
    inilogin['email']=email
    verifikasi=str(input("\nYakin Data Diri Sudah Benar? [Y=yes/N=no?]  : "))
    if verifikasi=="y" or verifikasi=="Y":
        print("\nLogin berhasil!")
    elif verifikasi=="n" or verifikasi=="N":
        login()
    os.system("pause")

#KEMBALI
def menukembali():
        os.system("cls")
        pembatas_()
        print(" Mau Kembali ke? ".center(46, "="))
        pembatas_()
        print("1. Menu Utama            ")
        print("2. Menu Game     ")
        pilihan_kembali = int(input("Masukkan Pilihan: "))
        if pilihan_kembali==1:
            menuutama()
        if pilihan_kembali==2:
            menugamebersama()
        os.system("pause")

#KEMBALI PEMBELIAN TIKET FANSIGN
def kembalifansign():
        # os.system("cls")
        pembatas_()
        print(" Mau Kembali ke? ".center(46, "="))
        pembatas_()
        print("1. Menu Pembelian Album            ")
        print("2. Menu Utama Fansign              ")
        pilihan_kembali = int(input("Masukkan Pilihan: "))
        if pilihan_kembali==1:
            pembelian_album()
        elif pilihan_kembali==2:
            menu_fansign()
        # os.system("pause")

#1.1_Pilihan Group
def daftargroup():
        pembatas_()
        print(" DAFTAR BOY & GIRLGROUP ".center(46, "-"))
        pembatas_()
        print("1. SHINee             ")
        print("2. EXO      ")
        print("3. Red Velvet")
        print("4. NCT |NCT 127, NCT U, NCT DREAM, WAYV|")
        print("5. aespa")
        print("0. Kembali")
        # kembali = print("Ingin Kembali? [Y(yes)/N(no)]?: ")
        # if kembali == "Y" or "y":
        #     menuutama()
        # elif kembali == "N" or "n":
        #     daftargroup()
        # os.system("cls")
        # os.system("pause")

def daftarboygirl():
        os.system("pause")
        pembatas_()
        print(" DAFTAR BOY & GIRLGROUP ".center(46, "-"))
        pembatas_()
        print("1. SHINee             ")
        print("2. EXO      ")
        print("3. Red Velvet")
        print("4. NCT |NCT 127, NCT U, NCT DREAM, WAYV|")
        print("5. aespa")
        print("0. Kembali")
        kembali = print("Ingin Kembali? [Y(yes)/N(no)]?: ")
        if kembali == "Y" or "y":
            menuutama()
        elif kembali == "N" or "n":
            daftarboygirl()
        # os.system("pause")

def shinee():
    print("\n")
    pembatas3_()
    print(" ALBUM SHINEE ".center(67, "*"))
    pembatas3_()
    shinee=dict(harga1=379000, harga2=230000)
    print("1. 7th Album [Don't Call Me] (Photobook Ver.)         |", shinee.get("harga1"), "|       ")
    print("2. 2nd Mini Album [Dice] (Digipack Ver.) SHINee-Onew  |", shinee.get("harga2"), "|        ")
    pilihan=int(input("\nMau beli album apa [1/2]?: "))
    album['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("7th Album [Don't Call Me] (Photobook Ver.)")
    elif pilihan==2:
        print("2nd Mini Album [Dice] (Digipack Ver.) SHINee-Onew")
    jumlah = int(input("Beli berapa?: "))
    album['jumlah']=jumlah
    pembatas3_()
    if pilihan==1:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "seharga", shinee.get("harga1"),"dengan jumlah", jumlah)
    elif pilihan==2:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "seharga", shinee.get("harga2"), "dengan jumlah", jumlah)
    lanjut= input("Mau beli album lagi [Y=yes/N=no?]: ")
    if lanjut=="y" or "Y":
        pembelian_album()
    elif lanjut=="n" or "N":
        kembalifansign()


def EXO():
    print("\n")
    pembatas3_()
    print(" ALBUM EXO ".center(73, "*"))
    pembatas3_()
    exo=dict(harga1=379000, harga2=230000)
    print("1. Special Album [Don't Fight The Feeling] (Photobook Ver.)   |", exo.get("harga1"), "|       ")
    print("2. 2nd Mini Album [Grey Suit] (Digipack Ver.) EXO-Suho        |", exo.get("harga2"), "|        ")
    pilihan=int(input("\nMau beli album apa [1/2]?: "))
    album['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("Special Album [Don't Fight The Feeling] (Photobook Ver.))")

    if pilihan==2:
        print("2nd Mini Album [Grey Suit] (Digipack Ver.) EXO-Suho")
    jumlah = int(input("Beli berapa?: "))
    album['jumlah']=jumlah
    pembatas3_()
    if pilihan==1:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "seharga", exo.get("harga1"),"dengan jumlah", jumlah)
    elif pilihan==2:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "seharga", exo.get("harga2"), "dengan jumlah", jumlah)

    lanjut= input("Mau beli album lagi [Y=yes/N=no?]: ")
    if lanjut=="y" or "Y":
        pembelian_album()
    if lanjut=="n" or "N":
        kembalifansign()

def redvelvet():
    print("\n")
    pembatas4_()
    print(" ALBUM RED VELVET ".center(90, "*"))
    pembatas4_()
    redvelvet=dict(harga1=428000,harga2=253000)
    print("1. Mini Album [The ReVe Festival 2022 : Feel My Rhythm] (Photobook Ver.)       |",redvelvet.get("harga1") , "|       ")
    print("2. Mini Album [The ReVe Festival 2022 : Birthday] (Digipack Ver.) Red Velvet   |",redvelvet.get("harga2"), "|        ")
    pilihan=int(input("\nMau beli album apa [1/2]?: "))
    album['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("Mini Album [The ReVe Festival 2022 : Feel My Rhythm] (Photobook Ver.)))")
    if pilihan==2:
        print("Mini Album [The ReVe Festival 2022 : Birthday] (Digipack Ver.) Red Velvet")
    jumlah = int(input("Beli berapa?: "))
    album['jumlah']=jumlah
    pembatas3_()
    if pilihan==1:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "seharga", redvelvet.get("harga1"),"dengan jumlah", jumlah)
    elif pilihan==2:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "seharga", redvelvet.get("harga2"), "dengan jumlah", jumlah)

    lanjut= input("Mau beli album lagi [Y=yes/N=no?]: ")
    if lanjut=="y" or "Y":
        pembelian_album()
    elif lanjut=="n" or "N":
        kembalifansign()

def nct():
    print("\n")
    pembatas3_()
    print(" ALBUM NCT ".center(73, "*"))
    pembatas3_()
    nct=dict(harga1=428000,harga2=226000, harga3=230000, harga4=352000, harga5=421000, harga6=230000)
    print("1. Winter Special Mini Album [Candy] (Digipack Ver.) NCT Dream  |", nct.get("harga1"), "|       ")
    print("2. The 4th Album [Jilju (2 Baddies)] (Digipack Ver.) NCT 127    |", nct.get("harga2"), "|        ")
    print("3. 4th Mini Album [Phantom] (Digipack Ver.) WAYV                |", nct.get("harga3"), "|        ")
    print("4. 4th Mini Album [Phantom] (Photobook Ver.) WAYV               |", nct.get("harga4"), "|        ")
    print("5. The 4th Album [Jilju (2 Baddies)] (Photobook Ver.) NCT 127   |", nct.get("harga5"), "|        ")
    print("6. Winter Special Mini Album [Candy] (Photobook Ver.) NCT Dream |", nct.get("harga6"), "|        ")
    pilihan=int(input("\nMau beli album apa [1-6]: "))
    album['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("Winter Special Mini Album [Candy] (Digipack Ver.) NCT Dream")
    elif pilihan==2:
        print("The 4th Album [Jilju (2 Baddies)] (Digipack Ver.) NCT 127")
    elif pilihan==3:
        print("4th Mini Album [Phantom] (Digipack Ver.) WAYV")
    elif pilihan==4:
        print("4th Mini Album [Phantom] (Photobook Ver.) WAYV")
    elif pilihan==5:
        print("The 4th Album [Jilju (2 Baddies)] (Photobook Ver.) NCT 127 ")
    elif pilihan==6:
        print("Winter Special Mini Album [Candy] (Photobook Ver.) NCT Dream")

    jumlah = int(input("Beli berapa?: "))
    album['jumlah']=jumlah
    pembatas3_()
    if pilihan==1:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", nct.get("harga1"))
    elif pilihan==2:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", nct.get("harga2"))
    elif pilihan==3:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", nct.get("harga3"))
    elif pilihan==4:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", nct.get("harga4"))
    elif pilihan==5:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", nct.get("harga5"))
    elif pilihan==6:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", nct.get("harga6"))

    lanjut= input("Mau beli album lagi [Y/N]?: ")
    if lanjut=="y" or "Y":
        pembelian_album()
    elif lanjut=="n" or "N":
        kembalifansign()

def aespa():
    print("\n")
    pembatas3_()
    print(" ALBUM AESPA ".center(73, "*"))
    pembatas3_()
    aespa=dict(harga1=330000, harga2=256000)
    print("1. 2nd Mini Album [Girls] (Photobook Ver.) Aespa  |", aespa.get("harga1"), "|       ")
    print("2. 2nd Mini Album [Girls] (Digipack Ver.)  Aespa  |", aespa.get("harga2"),"|        ")
    pilihan=int(input("\nMau beli album apa [1/2]?: "))
    album['pilihan']=pilihan
    if pilihan==1:
        pilihan
        print("2nd Mini Album [Girls] (Photobook Ver.) Aespa)")
    elif pilihan==2:
        print("2nd Mini Album [Girls] (Digipack Ver.)  Aespa")
    jumlah = int(input("Beli berapa?: "))
    album['jumlah']=jumlah
    pembatas3_()
    if pilihan==1:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", aespa.get("harga1"))
    elif pilihan==2:
        print("Berhasil membeli album pilihan", album.get("pilihan"), "dengan jumlah", jumlah, "seharga", aespa.get("harga2"))
    lanjut= input("Mau beli album lagi [Y/N]?: ")
    if lanjut=="y" or "Y":
        pembelian_album()
    elif lanjut=="n" or "N":
        kembalifansign()

#2. Pembelian Merchant
def pembelian_merchant():
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
            
    def daftarboygirl1():
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
            pilihan= input("Masukkan Pilihan [1-7]: ")
            if pilihan== '1':
                NCT_Dream()
            elif pilihan=='2':
                NCT_127()
            elif pilihan=='3':
                WAYV()
            elif pilihan=='4':
                EXO()
            elif pilihan=='5':
                SHINee()
            elif pilihan=='6':
                RedVelvet()
            elif pilihan=='7':
                Aespa()
            elif pilihan=='0':
                menuutama()

    def NCT_Dream():
        os.system("cls")
        print("\n")
        pembatas()
        print(" Group NCT Dream ".center(110, "*"))
        pembatas()
        nctdrm=dict(harga1=105000, harga2=660000, harga3=165000, harga4=295000, harga5=234000, harga6=700000, harga7=180000, 
                    harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", nctdrm.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", nctdrm.get("harga2"), "|        ")
        print("3. Danji Key Ring                                                                                   |", nctdrm.get("harga3"), "|        ")
        print("4. Winter Special Mini Album [Candy] (Photobook Ver.)                                               |", nctdrm.get("harga4"), "|        ")
        print("5. Winter Special Mini Album [Candy] (Digipack Ver.)                                                |", nctdrm.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", nctdrm.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", nctdrm.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", nctdrm.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", nctdrm.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", nctdrm.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", nctdrm.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", nctdrm.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", nctdrm.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", nctdrm.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    def NCT_127():
        os.system("clc")
        print("\n")
        pembatas()
        print(" Group NCT 127 ".center(110, "*"))
        pembatas()
        nct127=dict(harga1=105000, harga2=660000, harga3=280000, harga4=412000, harga5=226000, harga6=700000, harga7=180000, 
                    harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", nct127.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", nct127.get("harga2"), "|        ")
        print("3. Acrylic Stand Key Ring                                                                           |", nct127.get("harga3"), "|        ")
        print("4. The 4th Album [Jilju (2 Baddies)] (Photobook Ver.)                                               |", nct127.get("harga4"), "|        ")
        print("5. The 4th Album [Jilju (2 Baddies)] (Digipack Ver.)                                                |", nct127.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", nct127.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", nct127.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", nct127.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", nct127.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", nct127.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", nct127.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", nct127.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", nct127.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", nct127.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

            
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    def WAYV():
        os.system("cls")
        print("\n")
        pembatas()
        print(" Group WAYV ".center(110, "*"))
        pembatas()
        wayv=dict(harga1=105000, harga2=700000, harga3=245000, harga4=352000, harga5=230000, harga6=700000, harga7=180000, 
                    harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", wayv.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", wayv.get("harga2"), "|        ")
        print("3. Acrylic Key Ring                                                                                 |", wayv.get("harga3"), "|        ")
        print("4. 4th Mini Album [Phantom] (Photobook Ver.)                                                        |", wayv.get("harga4"), "|        ")
        print("5. 4th Mini Album [Phantom] (Digipack Ver.)                                                         |", wayv.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", wayv.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", wayv.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", wayv.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", wayv.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", wayv.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", wayv.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", wayv.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", wayv.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", wayv.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
                # os.system("pause")
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    def EXO():
        os.system("cls")
        print("\n")
        pembatas()
        print(" Group EXO ".center(110, "*"))
        pembatas()
        exo=dict(harga1=105000, harga2=580000, harga3=300000, harga4=379000, harga5=264000, harga6=700000, harga7=180000, 
                    harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", exo.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", exo.get("harga2"), "|        ")
        print("3. Voice Key Ring                                                                                   |", exo.get("harga3"), "|        ")
        print("4. Special Album [Don't Fight The Feeling] (Photobook Ver.)                                         |", exo.get("harga4"), "|        ")
        print("5. 2nd Mini Album [Grey Suit] (Digipack Ver.)                                                       |", exo.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", exo.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", exo.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", exo.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", exo.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", exo.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", exo.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", exo.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", exo.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", exo.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
                # os.system("pause")
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    def SHINee():
        os.system("cls")
        print("\n")
        pembatas()
        print(" Group SHINee ".center(73, "*"))
        pembatas4()
        shinee=dict(harga1=105000, harga2=585000, harga3=150000, harga4=332000, harga5=230000, harga6=700000, harga7=180000, 
                    harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", shinee.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", shinee.get("harga2"), "|        ")
        print("3. Acrylic Key Ring                                                                                 |", shinee.get("harga3"), "|        ")
        print("4. 7th Album [Don't Call Me] (Photobook Ver.)                                                       |", shinee.get("harga4"), "|        ")
        print("5. 2nd Mini Album [Dice] (Digipack Ver.)                                                            |", shinee.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", shinee.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", shinee.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", shinee.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", shinee.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", shinee.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", shinee.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", shinee.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", shinee.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", shinee.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
                # os.system("pause")
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    def RedVelvet():
        os.system("cls")
        print("\n")
        pembatas()
        print(" Group Red Velvet".center(110, "*"))
        pembatas()
        redve=dict(harga1=105000, harga2=615000, harga3=160000, harga4=428000, harga5=253000, harga6=700000, harga7=180000, 
                    harga8=95000, harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", redve.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", redve.get("harga2"), "|        ")
        print("3. Acrylic Key Ring                                                                                 |", redve.get("harga3"), "|        ")
        print("4. Mini Album [The ReVe Festival 2022 : Feel My Rhythm] (Photobook Ver.)                            |", redve.get("harga4"), "|        ")
        print("5. Mini Album [The ReVe Festival 2022 : Birthday] (Digipack Ver.)                                   |", redve.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", redve.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", redve.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", redve.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", redve.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", redve.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", redve.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", redve.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", redve.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", redve.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
                # os.system("pause")
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    def Aespa():
        os.system("cls")
        print("\n")
        pembatas()
        print(" Group Aespa ".center(110, "*"))
        pembatas()
        aespa=dict(harga1=105000, harga2=649000, harga3=250000, harga4=330000, harga5=256000, harga6=700000, harga7=180000, harga8=95000,
                harga9=650000, harga10=600000, harga11=215000, harga12=425000, harga13=125000, harga14=445000)
        print("1. 4x6 Photo + Photo Card Set                                                                       |", aespa.get("harga1"), "|        ")
        print("2. Lightstick                                                                                       |", aespa.get("harga2"), "|        ")
        print("3. Acrylic Stand Key Ring                                                                           |", aespa.get("harga3"), "|        ")
        print("4. 2nd Mini Album [Girls] (Photobook Ver.)                                                          |", aespa.get("harga4"), "|        ")
        print("5. 2nd Mini Album [Girls] (Digipack Ver.)                                                           |", aespa.get("harga5"), "|        ")
        print("6. Mood Lamp                                                                                        |", aespa.get("harga6"), "|        ")
        print("7. Cup                                                                                              |", aespa.get("harga7"), "|        ")
        print("8. Sticker                                                                                          |", aespa.get("harga8"), " |        ")
        print("9. Sling Bag                                                                                        |", aespa.get("harga9"), "|        ")
        print("10. T-Shirt                                                                                         |", aespa.get("harga10"), "|        ")
        print("11. Tumbler                                                                                         |", aespa.get("harga11"), "|        ")
        print("12. Hat                                                                                             |", aespa.get("harga12"), "|        ")
        print("13. Pop Socket                                                                                      |", aespa.get("harga13"), "|        ")
        print("14. Casing                                                                                          |", aespa.get("harga14"), "|        ")
        pilihan=int(input("\nMau beli product apa [1-14]?: "))
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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
                lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

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
                # os.system("pause")
            lanjut= input("Mau beli lagi [Y/N]?: ")
            if lanjut=="y" or "Y":
                daftarboygirl1()
            elif lanjut=="n" or "N":
                menuutama()

    #1_PEMBELIAN ALBUM 
    def pembelian_merchant():
        os.system("cls")
        pembatas()
        print(" Pembelian Merchandise ".center(110, "="))
        daftarboygirl()
        pilihangroup=int(input("Masukkan grup yang dipilih [1-7]: "))
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
        print("1. Pembelian dan Pembayaran Merchandise")
        print("2. Keluar Dari SM Store Official")
        pembatas()
        pilihan= input("Pilih Menu : ")
        if pilihan == "1":
            pembelian_merchant()
        if pilihan == "2":
            pembatas()
            print('Terimakasih Telah Berbelanja Disini'.center(110, "="))
            menuutama()
            pembatas()
            
    menu_SM_store()    

    
#3. Pemesanan Tiket Konser
def pemesanan_tiket_konser():
    #PEMESANAN TIKET KONSER
    def pemesanan_tiket():
        os.system('cls')
        garis4()
        print('Pemesanan Tiket'.center(46,'='))
        garis4()
        print('\n1. Pilihan Day Konser')
        print('2. Pilihan Group Konser')
        print('3. Pilihan Seatplan Konser')
        pilihan_menu=int(input('\nPilih Menu : '))
        if pilihan_menu==1:
            day_konser()
        elif pilihan_menu==2:
            group_konser()
        elif pilihan_menu==3:
            seatplan_konser()
        else:
            print('Gagal Melakukan Pemesanan Tiket')
        os.system('pause')

    # 1. Memilih Hari Konser
    def day_konser():
        print('\n')
        print('Memilih Day Konser'.center(46,'-'))
        p_hari = ['Day 1','Day 2']
        pilih_hari = enumerate(p_hari, 1)
        for index, p_hari in pilih_hari:
            print(f"\nPilihan {index} : {p_hari}")
        pilih_hari=str(input('\nPilih day konser: '))
        tiket['day']=pilih_hari
        if pilih_hari == ('Day 1'):
            return True
        elif pilih_hari == ('Day 2'):
            return True
        else:
            return False

    # 2. Memilih Group Konser
    def group_konser():
        print('\n')
        print('Memilih Group Konser'.center(46,'-'))
        p_group = ['EXO', 'Red Velvet', 'NCT 127', 'NCT Dream',
                'WAYV', 'Aespa', 'SHINee']
        pilih_group = enumerate(p_group, 1)
        for index, p_group in pilih_group:
            print(f"\nPilihan {index} : {p_group}")
        pilih_group=str(input('\nPilih group konser: '))
        tiket['group']=pilih_group
        if pilih_group == ('EXO'):
            return True
        elif pilih_group == ('Red Velvet'):
            return True
        elif pilih_group == ('NCT 127'):
            return True
        elif pilih_group == ('NCT Dream'):
            return True
        elif pilih_group == ('WAYV'):
            return True
        elif pilih_group == ('Aespa'):
            return True
        elif pilih_group == ('SHINee'):
            return True
        else:
            return False

    # 3. Memilih Seatplan Konser
    def seatplan_konser():
        print('\n')
        print('Memilih Seatplan Konser'.center(46,'-'))
        p_seatplan = ['CAT 4 Seating', 'CAT 3 Standing',
                    'CAT 2 Standing', 'CAT 1 Seating']
        pilih_seatplan = enumerate (p_seatplan, 1)
        for index, p_seatplan in pilih_seatplan:
            print(f"\nPilihan {index} : {p_seatplan}")
        pilih_seatplan=str(input('\nPilih seatplan konser: '))
        tiket['seatplan']=pilih_seatplan
        if pilih_seatplan == ('CAT 4 Seating'):
            return True
        elif pilih_seatplan == ('CAT 3 Standing'):
            return True
        elif pilih_seatplan == ('CAT 2 Standing'):
            return  True
        elif pilih_seatplan == ('CAT 1 Seating'):
            return True
        else:   
            return False

    # PEMBELIAN TIKET
    def pembelian_tiket():
        os.system('cls')
        garis4()
        print('Pembelian Tiket'.center(46,'='))
        garis4()
        print('\n1. Harga Tiket')
        print('2. Jumlah Tiket')
        print('3. Pembayaran Tiket')
        pilihan_menu=int(input('\nPilih Menu : '))
        if pilihan_menu==1:
            harga_tiket()
        elif pilihan_menu==2: 
            jumlah_tiket()
        elif pilihan_menu==3:
            bayar_tiket()
        else:
            print('Gagal Melakukan Pembelian Tiket')
        os.system('pause')    

    def harga_tiket():
    # 1. Memilih Harga Tiket
        print('\n')
        print('Memilih Harga Tiket Konser'.center(46,'-'))
        print('\n1. Rp. 1590000 = CAT 4 Seating')
        print('2. Rp. 1815000 = CAT 3 Standing')
        print('3. Rp. 2640000 = CAT 2 Standing')
        print('4. Rp. 2970000 = CAT 1 Seating')
        uang=int(input('\nPilih harga tiket [sesuai seatplan] : '))
        tiket['harga']=uang

    def jumlah_tiket():    
    # 2. Memilih Jumlah Tiket 
        print('\n')
        print('Memilih Jumlah Tiket Konser'.center(46,'-'))
        quantity=int(input('\nMasukkan jumlah tiket: '))
        tiket['jumlah']=quantity

    def bayar_tiket():
    #3. Melakukan Pembayaran Tiket
        print('\n')
        print('Melakukan Pembayaran Tiket Konser'.center(46,'-'))
        harga=int(input('\nMasukkan pembayaran tiket: '))
        tiket['bayar']=harga
        if tiket.get('harga') == 1590000:
            total_harga = 1590000*tiket.get('jumlah')
            print(tiket.get('jumlah'),"harga tiket = Rp",total_harga)
        elif tiket.get('harga') == 1815000:
            total_harga = 1815000*tiket.get('jumlah')
            print(tiket.get('jumlah'),"harga tiket = Rp",total_harga)
        elif tiket.get('harga') == 2640000:
            total_harga = 2640000*tiket.get('jumlah')
            print(tiket.get('jumlah'),"harga tiket = Rp",total_harga)
        elif tiket.get('harga') == 2970000:
            total_harga = 2970000*tiket.get('jumlah')
            print(tiket.get('jumlah'),"harga tiket = Rp",total_harga)
        else:
            print("pilihan tidak ada, silahkan pilih kembali")
        #validasi 
        if total_harga>=harga:
            print('Pembayaran tidak memenuhi, transaksi batal'.center(46,'='))
        else:
        #valid
            harga = int(tiket.get('bayar'))
            kembalian = int(harga-total_harga)
        #cetak
            print('Uang Anda Rp',harga)
            print('Kembalian Anda Rp',kembalian)
            print('Pembayaran memenuhi, transaksi berhasil'.center(46,'='))

    #CETAK TIKET
    def pencetakan_tiket():
        os.system('cls')
        garis1()
        garis1()
        print(' DAY 1/2 - SMTOWN 2023:SMCU PALACE @ KWANGYA '.center(69,'='))
        print('\n')
        print('KONSER -',tiket.get("group"))
        print('\nTanggal/Waktu          \n',tiket.get("day"))
        print('\nValiditas              \nBerlaku mulai 1 Januari 2023')
        print('\nLokasi                 \nStadion Utama Gelora Bung Karno, Jalan Pintu Satu Senayan,')
        print('Gelora, Central Jakarta City, Jakarta, Indonesia.')
        print('JAKARTA PUSAT, JAKARTA, INDONESIA 10270')
        print('\nTotal Tiket            \n',tiket.get("jumlah"))
        print('\nTipe Tiket             \n',tiket.get("seatplan"))
        print('\n')
        print(' TIKET BERHASIL DICETAK '.center(69,'='))
        garis1()
        garis1()
        print('Time stamp: ',now,)
    
    #KEMBALI
    def kembali1():
        os.system('cls')
        garis4()
        print('Pemesanan Tiket'.center(46,'='))
        garis4()
        print('\n1. Pilihan Hari Konser')
        print('2. Pilihan Group Konser')
        print('3. Pilihan Seatplan Konser')
        pilihan_kembali1 = int(input("\nKembali ke pilihan? : "))
        if pilihan_kembali1==1:
            day_konser()
        if pilihan_kembali1==2:
            group_konser()
        if pilihan_kembali1==3:
            seatplan_konser()
        os.system('pause')

    def kembali2():
        os.system('cls')
        garis4()
        print('Pemesanan Tiket'.center(46,'='))
        garis4()
        print('\n1. Pilihan Hari Konser')
        print('2. Pilihan Group Konser')
        print('3. Pilihan Seatplan Konser')
        pilihan_kembali2 = int(input("\nKembali ke pilihan? : "))
        if pilihan_kembali2==1:
            day_konser()
        if pilihan_kembali2==2:
            group_konser()
        if pilihan_kembali2==3:
            seatplan_konser()
        os.system('break')

    def kembali3():
        os.system('cls')
        garis4()
        print('Pembelian Tiket'.center(46,'='))
        garis4()
        print('\n1. Harga Tiket')
        print('2. Jumlah Tiket')
        print('3. Pembayaran Tiket')
        pilihan_kembali3=int(input("\nKembali ke pilihan?: "))
        if pilihan_kembali3==1:
            harga_tiket()
        if pilihan_kembali3==2: 
            jumlah_tiket()
        if pilihan_kembali3==3:
            bayar_tiket()
        os.system('pause')

    def kembali4():
        os.system('cls')
        garis4()
        print('Pembelian Tiket'.center(46,'='))
        garis4()
        print('\n1. Harga Tiket')
        print('2. Jumlah Tiket')
        print('3. Pembayaran Tiket')
        pilihan_kembali4 = int(input("\nKembali ke pilihan?: "))
        if pilihan_kembali4==1:
            harga_tiket()
        if pilihan_kembali4==2: 
            jumlah_tiket()
        if pilihan_kembali4==3:
            bayar_tiket()
        os.system('break')

    #UTAMA
    def menu_utama():
        import os
        while True:

            os.system('cls')
            garis1()
            garis0()
            print(' PEMBELIAN TIKET KONSER SMTOWN 2023:SMCU PALACE @ KWANGYA '.center(69,'='))
            garis0()
            garis1()
            print('\n1. Pemesanan Tiket')
            print('2. Pembelian Tiket')
            print('3. Cetak Tiket')
            print('0. Selesai')
            pilihan_menu=int(input('\nPilihlah Menu : '))
            if pilihan_menu==1:
                pemesanan_tiket()
                kembali1()
                kembali2()
            elif pilihan_menu==2:
                pembelian_tiket()
                kembali3()
                kembali4()
            elif pilihan_menu==3:
                pencetakan_tiket()
            elif pilihan_menu==0:
                os.system('cls')
                print(' SELAMAT MENONTON KONSER SMTOWN 2023:SMCU PALACE @ KWANGYA '.center(69,'='))  
                garis1()
                menuutama()
            else:
                os.system('cls')
                print(' TIDAK ADA PILIHAN LAIN, SILAHKAN MENCOBA LAGI '.center(69,'='))
                       
            os.system('pause')
    menu_utama() 


#4. Pemesanan Tiket Fansign 
#1_PEMBELIAN ALBUM 
def pembelian_album():
    os.system("cls")
    pembatas_()
    print(" Pembelian Album ".center(46, "="))
    daftargroup()
    pilihangroup=int(input("Masukkan grup yang dipilih: "))
    if pilihangroup == 1:
        shinee()
    elif pilihangroup == 2:
        EXO()
    elif pilihangroup == 3:
        redvelvet()
    elif pilihangroup == 4:
        nct()
    elif pilihangroup == 5:
        aespa()
    elif pilihangroup == 0:
        kembalifansign()
    os.system("pause")   
    

def pengundian_fansign():
    # os.system('pause')
    grup=['SHINee', 'EXO', 'Redvelvet', 'NCT 127', 'NCT U', 'NCT Dream', 'WAYV','aespa']
    tanggal=['10-10-2023', '11-10-23']
    x = rd.choice(grup)
    y = rd.randint(1, 1000)
    z = rd.randint(1, 1000)
    a = rd.choice(tanggal)
    def pembatas5():
        print("-"*20)
    pembatas4_()
    print("Mall Kota Kasablanka, Jakarta  :                           FANSIGN")
    pembatas4_()
    print("Tanggal                        : ",a,"                                    ")
    print("Group                          : ",x,"                               ")
    print("Seat                           : ",z,"                               ")
    pembatas4_()
    for i in range(1):
        print("Dengan nomor undian", y, "kamu mendapat seat nomor", z)
        print("\nSelamat! Kamu akan bertemu", x)
        pembatas5()
        print("Peringatan!".center(20, "="))
        pembatas5()
        print("Sangat disarankan untuk mengikuti S&K fansign agar bisa bertemu dengan", x, "dalam keadaan baik")
    kembali1= input("Mau kembali [Y(yes)/N(no)]?: ")
    if kembali1=="y" or "Y":
        menu_fansign()
    elif kembali1=="n" or "N":
        pass
    # menu_fansign() 


#MENU UTAMA FANSIGN    
def menu_fansign():
    # os.system("cls")
    # os.system("pause")
    pembatas_()
    print(" FANSIGN ".center(46, "="))
    pembatas_()
    print("1. Pembelian Album            ")
    print("2. Pengundian Fansign         ")
    print("0. Kembali Ke Menu Utama      ")
    pembatas_()
    pilihanfansign= input("Pilih Menu: ")
    if pilihanfansign == '1':
        pembelian_album()
    elif pilihanfansign == '2':
        pengundian_fansign()
    elif pilihanfansign == '0':
        menuutama()


#5. Game Bersama Bias 
def gamebersamabias():    
    def pembatas():
        print("-"*46)
    def pembatas2():
        print("="*46)

def cocokidol():
    os.system('cls')
    pembatas_()
    print(" COCOKIDOL ".center(46, "-"))
    pembatas_()
    grupcowok=['Key', 'Taemin', 'Minho', 'Baekhyun', 'Suho', 'Lay', 'D.O','Chen', 'Xiumin', 'Kai', 'Sehun', 'Chanyeol', 
    'Taeyong', 'Taeil', 'Doyoung', 'Kun', 'Jhonny', 'Yuta', 'Jaehyun', 'Lucas', 'Jungwoo', 'Mark', 'Haechan', 'Jaemin', 'Jeno',
    'Jisung', 'Chenle', 'Renjun', 'Ten', 'Hendry', 'Xiojun', 'Yangyang', 'Winwin']
    grupcewek=['Irene', 'Joy', 'Seulgi', 'Wendy', 'Yeri', 'Karina', 'Gissele','WInter', 'Ningning']
    print("Selamat Datang di Permainan COCOKIDOL")
    print("\nSiapakah yang cocok menjadi pasanganmu? ")
    kelamin = input("Jenis Kelamin Kamu[P/L]?: ")
    if kelamin == "P" or "p":
        untukcewek = rd.choice(grupcowok)
        print("\nIdol yang cocok menjadi pasanganmu adalah", untukcewek)
    else: 
        untukcowok = rd.choice(grupcewek)
        print("\nIdol yang cocok menjadi pasanganmu adalah", untukcowok)
    # ulangcocokidol= input("\nMau coba lagi [Y/N]?: ")
    # if ulangcocokidol=='y' or 'Y':
    #     print("\nSilahkan main lagi.\n")
    #     cocokidol()
    # elif ulangcocokidol == 'n' or 'N':
    #     #  ulangcocokidol=='n' or  'N':
    #     print("\nTerimakasih sudah main Tebak Angka ini.\n")
    #     menugamebersama()
    menu_fansign()

def guntingbatukertas():
        import random
        pembatas_()
        print("Hi", inilogin.get("namapanggilan"), "! Selamat datang di permainan Batu Gunting Kertas!")
        pembatas_()
        idol= input(str("Pilih Bias yang Ingin Kamu Ajak Main: "))
        bot=['batu', 'gunting', 'kertas']

        while True:
            x = random.choice(bot)
            data =input('\nMasukkan pilihanmu |Batu, Gunting, Kertas|: ')
            print("\n")
            if data.lower()==x:
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                print("===================")
                print("Hasil Seri")
                print("===================\n\n")

            #bagian menang
            elif data.lower() == 'batu' and x == 'gunting':
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                print("===================")
                print("Yeayy! Kamu menang!")
                print("===================\n\n")

            elif data.lower() == 'kertas' and x == 'batu':
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                #  print(f'Lawan memilih ---> {x.capitalize()}')
                print("===================")
                print("Yeayy! Kamu menang!")
                print("===================\n\n")

            elif data.lower() == 'gunting' and x == 'kertas':
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                print("===================")
                print("Yeayy! Kamu menang!")
                print("===================\n\n")


            #bagian kalah
            elif data.lower() == 'gunting' and x == 'batu':
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                print("===================")
                print("Yah:(((Kamu kalah dari", idol)
                print("===================\n\n")

            elif data.lower() == 'batu' and x == 'kertas':
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                print("===================")
                print("Yah:(((Kamu kalah dari", idol)
                print("===================\n\n")
            
            elif data.lower() == 'kertas' and x == 'gunting':
                print(f'Kamu memilih ---> {data.capitalize()}')
                print(idol, "memilih ---> ", x.capitalize())
                print("===================")
                print("Yah:(((Kamu kalah dari", idol)
                print("===================\n\n")
            else:
                print("Tolong masukkan pilihan yang tepat |Batu/Gunting/Kertas|\n")

            ulang= input("Mau main lagi [Y/N]?: ")
            # while(ulang!= 'y' and ulang!= 'Y'and ulang!='n' and ulang!= 'N'):
            #     ulang=input("Maaf inputan anda salah, silahkan coba lagi.\nMau main lagi: ")
            
            if ulang=='y' and ulang!= 'Y':
                print("\nSilahkan main lagi.\n")
                guntingbatukertas()

            else:
                print("\nTerimakasih sudah main Tebak Angka ini.\n")
                menukembali()
            
def menugamebersama():
        pembatas_()
        print(" GAME ".center(46, "="))
        pembatas_()
        print("1. Gunting Batu Kertas            ")
        print("2. COCOKIDOL    ")
        print("0. Keluar")

        pembatas_()
        pilihan= input("Pilih Menu: ")
        if pilihan == "1" or pilihan == "Gunting Batu Kertas":
            guntingbatukertas()
        elif pilihan == "2":
            cocokidol()
        elif pilihan == "0":
            menuutama()
#KELUAR
def keluar():
    # os.system('cls')
    keluar= input("Yakin Ingin Keluar [Y(yes)/N(no)]?: ")
    if keluar=='y' or 'Y':
        print("\nTerimakasih telah berkunjung ke SMTOWN APP\n")
    elif keluar=='n' or 'N':
        menuutama()
    os.system("pause")
#MENU
def sebelummenu():
    os.system("cls")
    print("Hi", inilogin.get("namapanggilan"), "welcome to SMTOWN APP!")
    # os.system("pause")

def menuutama():
        os.system("pause")
        pembatas_()
        print(" MENU ".center(46, "="))
        pembatas_()
        print("1. Daftar Boy/Girlgroup            ")
        print("2. Pembelian Merchandise Official     ")
        print("3. Pembelian Tiket Konser          ")
        print("4. Pembelian Tiket Fansign         ")
        print("5. Game Bersama Bias               ")
        print("0. Keluar")
        #PILIHAN
        pembatas_()
        pilihan= input("Pilih Menu: ")
        if pilihan == "1" or pilihan == "Daftar Boy/Girlgroup":
            daftarboygirl()
        elif pilihan == "2" or pilihan == "Pembelian Merchant Official":
            pembelian_merchant()
        elif pilihan == "3" or pilihan == "Pembelian Tiket Konser":
            pemesanan_tiket_konser()
        elif pilihan == "4" or pilihan == "Pembelian Tiket Fansign":
            menu_fansign()        
        elif pilihan == "5" or pilihan == "Game Bersama Bias":
            menugamebersama()
        elif pilihan == "0" or pilihan == "Keluar":
            keluar()
        else:
            print("Tolong masukkan pilihan yang tepat\n")
            pilihan= input("Pilih Menu: ")
            if pilihan == "1" or pilihan == "Daftar Boy/Girlgroup":
                daftarboygirl()
            elif pilihan == "2" or pilihan == "Pembelian Merchant Official":
                return pembelian_merchant()
            elif pilihan == "3" or pilihan == "Pembelian Tiket Konser":
                pemesanan_tiket_konser()
            elif pilihan == "4" or pilihan == "Pembelian Tiket Fansign":
                menu_fansign()        
            elif pilihan == "5" or pilihan == "Game Bersama Bias":
                menugamebersama()
            elif pilihan == "0" or pilihan == "Keluar":
                keluar()
            # print("\nTerimakasih")
        pembatas_()

# pembelian_merchant()
# pembelian_merchant()
login()
sebelummenu()
menuutama()