import module1
m1 = module1.tugasmodul4
print("Tugas Modul 4")
m1.PerkenalanKelompok(30,2)
m1.NamaAnggota("Rifky Hernanda", "Anas Noor Hakim", "Bagas Satrio Unggul Yudho", "Joanne Eva Donna")
m1.printgaris(0)
listbarang = []
hargabarang = []
jumlahbarang = []
jumlahhargaitem = []
totalharga = 0
n = 0
t = 0
while (n<=0):
    barang = str(input("masukkan nama barang : "))
    jumlah = int(input("masukkan jumlah barang : "))
    harga  = int(input("masukkan harga barang : "))
    listbarang = listbarang + [barang]
    jumlahbarang = jumlahbarang + [jumlah]
    hargabarang  = hargabarang + [harga]
    hargaitem = 0
    hargaitem = jumlah * harga
    jumlahhargaitem = jumlahhargaitem + [hargaitem]
    totalharga = totalharga + hargaitem
    lanjut = str(input("Masukkan barang lagi?(ya/tidak) : "))
    t +=1
    if lanjut == 'tidak':
        n +=1
for x in range(t):
    m1.printgaris(50)
    p = x+1
    print("Nama barang ",(p),": ",listbarang[x])
    print("jumlah barang :",jumlahbarang[x])
    print("harga barang :",hargabarang[x])
    print("total harga barang :", jumlahhargaitem[x])
m1.printgaris(50)
print("Total yang harus dibayarkan adalah : Rp.",(totalharga))


