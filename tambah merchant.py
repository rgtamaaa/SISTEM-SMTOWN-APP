import koneksi as k
import os

def inputData():
    print("===== MENAMBAHKAN DATA PRODUCT =====\n")
    no      = input("No      : ")
    product = input("Product : ")
    group   = input("Group   : ")
    price   = int(input("Price   : "))

    sql = "INSERT INTO merchant VALUES (%s,%s,%s,%s)"
    val = (no, product, group, price)
    cursor = k.konek.cursor()
    cursor.execute(sql,val)
    k.konek.commit()
    print(cursor.rowcount, "Data Product Berhasil Ditambahkan")

lagi="Y"
while lagi=="y" or lagi=="Y":
    os.system('cls')
    inputData()
    lagi=input("Tambah data lagi? [Y/T] : ")