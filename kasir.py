import os
import koneksi as rca
import mysql.connector
from mysql.connector import Error
import datetime
now=datetime.datetime.now()

try:
    konek = mysql.connector.connect(host='localhost',
                                    database='daftar_barang',
                                    user='regita_cahya',
                                    password='1412123')
except Error as e:
    print("Terjadi Kesalahan ", e)

def pembayaran():
    kode=str(input('kode : '))
    jumlah=int(input('jumlah : '))
    cursor = rca.konek.cursor()
    sql = "SELECT * FROM mixue WHERE kode LIKE %s"
    val = (kode)
    harga = "SELECT * FROM mixue WHERE harga LIKE %s"
    total=jumlah+harga
    bayar=int(input('Cash : '))
    change=bayar-total    
    cursor.execute(sql, val)
    print('MIXUE'.center(46))
    print('Kubangpari City'.center(46))
    print('\n',now)
    print('\n----------------------------------------------\n')
    hasil = cursor.fetchall()
    if cursor.rowcount < 0:
            print("Tidak ada data")
    else:
        print("--------------------------------------------------------------------------")
        print(" Item                            Price                       QIY            AMT  ")
        no=0
        for x in hasil : 
            no+=1
            print("{:3d}".jenis_ice(x[0]),
                  "{:24s}|".format(x[1]),
                  "{:15s}       |".format(x[2]),
                  "{:^8d}|".format(x[3]))
        print("+-----------------+-------------------------+-----------------------+---------+")



pembayaran()