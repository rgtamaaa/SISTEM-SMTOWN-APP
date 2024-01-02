import mysql.connector
from mysql.connector import Error

try:
    konek = mysql.connector.connect(host='localhost',
                                    database='pembelian_merchant',
                                    user='root',
                                    password='')
    #meminta koneksi
    if konek.is_connected():
        db_Info = konek.get_server_info()
        print("Koneksi ke MySQL server versi : ",db_Info)
        cursor = konek.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Anda telah Koneksi ke Database :", record)
#cek jika terjadi kesalahan
except Error as e:
    print("Terjadi Kesalahan ", e)