import koneksi

try:
    sql = """ CREATE TABLE merchant (
        no int(11) NOT NULL,
        customer varchar(50),
        group varchar(50),
        product varchar(20),
        price int(11),
        quantity int(11),
        PRIMARY KEY(id)) """
    cursor = koneksi.konek.cursor()
    result = cursor.execute(sql)
    print("Tabel Merchant Berhasil Dibuat")

except koneksi.Error as e:
    print("Terjadi Kesalahan ", e)
finally:
    if koneksi.konek.is_connected():
        cursor.close()
        koneksi.konek.close()
        print("Koneksi ke MySQL Telah Ditutup")