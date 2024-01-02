# PEMBELIAN TIKET KONSER

#DATETIME
import datetime
now=datetime.datetime.now()
import os

#DICTIONARY
tiket=dict(
    day="",
    group="",
    seatplan="",
    harga=0,
    jumlah=0,
    bayar=0,
)
#PEMESANAN TIKET
def pemesanan_tiket():
    print('\nPemesanan Tiket\n')
    print('1. Pilihan Hari Konser')
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

# 1. Memilih Hari Konser
def day_konser():
    print('\nMemilih Day Konser SMTOWN 2023\n')
    p_hari = ['Day 1','Day 2']
    pilih_hari = enumerate(p_hari, 1)
    for index, p_hari in pilih_hari:
        print(f"Pilihan {index} : {p_hari}")
    pilih_unit=str(input('\nPilih day konser : '))
    tiket['day']=pilih_hari
    if pilih_unit == ('Day 1'):
        return True
    elif pilih_unit == ('Day 2'):
        return True
    else:
        pemesanan_tiket()
       
    pemesanan_tiket()

# 2. Memilih Group Konser
def group_konser():
    print('\nMemilih Group Konser SMTOWN 2023\n')
    p_group = ['EXO', 'Red Velvet', 'NCT 127', 'NCT U', 'NCT Dream',
               'WAYV', 'Aespa', 'Got the Beat', 'SHINee']
    pilih_group = enumerate(p_group, 1)
    for index, p_group in pilih_group:
        print(f"Pilihan {index} : {p_group}")
    pilih_group=str(input('\nPilih group konser : '))
    tiket['group']=pilih_group
    if pilih_group == ('EXO'):
        return True
    elif pilih_group == ('Red Velvet'):
        return True
    elif pilih_group == ('NCT 127'):
        return True
    elif pilih_group == ('NCT U'):
        return True
    elif pilih_group == ('NCT Dream'):
        return True
    elif pilih_group == ('WAYV'):
        return True
    elif pilih_group == ('Aespa'):
        return True
    elif pilih_group == ('Got the Beat'):
        return True
    elif pilih_group == ('SHINee'):
        return True
    else:
        return False

    

# 3. Memilih Seatplan Konser
def seatplan_konser():
    print('\nMemilih Seatplan Konser SMTOWN 2023\n')
    p_seatplan = ['CAT 4 Seating', 'CAT 3 Standing', 'CAT 2 Standing', 'CAT 1 Seating']
    pilih_seatplan = enumerate (p_seatplan, 1)
    for index, p_seatplan in pilih_seatplan:
        print(f"Pilihan {index} : {p_seatplan}")
    pilih_seatplan=str(input('\nPilih seatplan konser : '))
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

# Pembelian Tiket
def pembelian_tiket():
    print('\nPembelian Tiket\n')
    print('1. Harga Tiket')
    print('2. Jumlah Tiket')
    print('3. Pembayaran Tiket')
    pilihan_menu=int(input('\nPilih Menu : '))
    if pilihan_menu==1:
       harga_tiket()
    elif pilihan_menu==2: 
        jumlah_tiket()
    elif pilihan_menu==3:
       bayar_tiket()
    elif pilihan_menu==0:
        menu_utama()
    else:
       print('Gagal Melakukan Pembelian Tiket') 

def harga_tiket():
# 1. Memilih Harga Tiket 
    print('\nMemilih Harga Tiket Konser SMTOWN 2023\n')
    print('1. Rp. 1590000 = CAT 4 Seating')
    print('2. Rp. 1815000 = CAT 3 Standing')
    print('3. Rp. 2640000 = CAT 2 Standing')
    print('4. Rp. 2970000 = CAT 1 Seating')
    uang=int(input('Pilih harga tiket [sesuai seatplan] : '))
    tiket['harga']=uang

def jumlah_tiket():    
# 2. Memilih Jumlah Tiket 
    print('\nMemilih Jumlah Tiket Konser SMTOWN 2023\n')
    quantity=int(input('Masukkan jumlah tiket: '))
    tiket['jumlah']=quantity

def bayar_tiket():
#3. Melakukan Pembayaran Tiket
    print('\nMelakukan Pembayaran Tiket Konser SMTOWN 2023\n')
    harga=int(input('Masukkan pembayaran tiket: '))
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
        print('================ Pembayaran tidak memenuhi, transaksi batal ================')
    else:
    #valid
        harga = int(total_harga)
        tiket['total']=total_harga
        kembalian = int(harga-total_harga)
        tiket['sisa']=kembalian
    #cetak
        print('Uang anda Rp',harga)
        print('Kembalian anda Rp',kembalian)
        print('================== Pembayaran memenuhi, transaksi berhasil ==================')

#Cetak Tiket
def pencetakan_tiket():
    print('\nPencetakan Tiket\n')
    cetak_tiket()

def garis():
    print('='*69)

def cetak_tiket():
    garis()
    garis()
    print('DAY 1/2 - SMTOWN 2023:SMCU PALACE @ KWANGYA'.center(69,'='))
    print('\nTanggal/Waktu          \n ',tiket.get("day"))
    print('\nValidatas              \nBerlaku di 1 Januari 2023')
    print('\nLokasi                 \nStadion Utama Gelora Bung Karno')
    print('\nTotal Tiket            \n ', tiket.get("quantity"))
    print('\nTipe Tiket             \n ',tiket.get("seatplan"))
    print('TIKET BERHASIL DICETAK'.center(69,'='))
    garis()
    garis()
    print('Time stamp: ',now,)

# def pemesanan_tiket():
#     print('\nPemesanan Tiket\n')
#     print('1. Pilihan Hari Konser')
#     print('2. Pilihan Group Konser')
#     print('3. Pilihan Seatplan Konser')
#     pilihan_menu=int(input('\nPilih Menu : '))
#     if pilihan_menu==1:
#         day_konser()
#     elif pilihan_menu==2:
#         group_konser()
#     elif pilihan_menu==3:
#         seatplan_konser()
#     else:
#         print('Gagal Melakukan Pemesanan Tiket') 
  
#def pembelian_tiket():
#   print('\nPembelian Tiket\n')
#    print('1. Harga Tiket')
#   print('2. Jumlah Tiket')
#   print('3. Pembayaran Tiket')#    print('0. Menu')
#   pilihan_menu=int(input('\nPilih Menu : '))
#   if pilihan_menu==1:
#       harga_tiket()
#     elif pilihan_menu==2: #       jumlah_tiket()
#    elif pilihan_menu==3:
#        bayar_tiket()
#    elif pilihan_menu==0:
#        menu_utama()
#    else:
#       print('Gagal Melakukan Pembelian Tiket')  

#def pencetakan_tiket():
#    print('\nPencetakan Tiket\n')
#    cetak_tiket()

#UTAMA
def menu_utama():
    import os

    while True:

        os.system("cls")
        print('PEMBELIAN TIKET KONSER SMTOWN 2023:SMCU PALACE @ KWANGYA\n')
        print('1. Pemesanan Tiket')
        print('2. Pembelian Tiket')
        print('3. Cetak Tiket')
        print('0. Selesai')
        pilihan_menu=int(input('\nPilihlah Menu : '))
        if pilihan_menu==1:
            pemesanan_tiket()
            continue
        elif pilihan_menu==2:
            pembelian_tiket()
            continue
        elif pilihan_menu==3:
            pencetakan_tiket()
            continue
        else:
            print('\nTERIMA KASIH, SELAMAT MENONTON KONSER  SMTOWN 2023:SMCU PALACE @ KWANGYA')
            break
        os.system("pause")
menu_utama()        