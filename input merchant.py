import koneksi

try: 
    sql = """INSERT INTO merchant(No,Product,Group,Price)
    VALUES('1','4x6 Photo + Photo Card Set','NCT Dream',105000)"""
    cursor = koneksi.konek.cursor()
    result = cursor.execute(sql)
    koneksi.konek.commit()
    print("Berhasil menambahkan tabel merchant sebanyak =",cursor.rowcount,"rekaman")
except koneksi.Error as e:
    print("Terjadi kesalahan ", e)
finally:
    if koneksi.konek.is_connected():
        cursor.close()
        koneksi.konek.close()
        print("Koneksi ke MySQL telah ditutup")