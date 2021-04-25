import decode
d1 = decode.buatdecode
def encode(kalimat):
  abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      nomor_lama = abjad.index(karakter)
      #karena jumlah karakter hanya ada 26 jadi diulang lah, dan jadi +4
      nomor_baru = (nomor_lama + 4 ) % len(abjad)
      abjad_baru = abjad[nomor_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode
n = 0
while(n<1):
    pilihan = input("apa yang mau kamu lakukan? (pilih 1 untuk enkripsi, 2 untuk dekripsi, 3 untuk keluar) : ")
    if pilihan == '1':
        kalimat = input('Masukkan kalimat yang ingin dienkripsi : ')
        hasil = encode(kalimat)
        print('kalimat :',kalimat," berhasil di enkripsi menjadi :",hasil)
        lanjut = input("lanjutkan program(iya/tidak): ")
        if lanjut == 'iya':
            n = 0
        elif lanjut == 'tidak':
            n +=2
    elif pilihan == '2':
        kalimat = input('Masukkan kalimat yang ingin didekripsi : ')
        hasil = d1.decodex(kalimat)
        print('kalimat :',kalimat," berhasil di dekripsi menjadi :",hasil)
        lanjut = input("lanjutkan program(iya/tidak): ")
        if lanjut == 'iya':
            n = 0
        elif lanjut == 'tidak':
            n +=2
    elif pilihan == '3':
        n+=1
    else:
        print("masukkan antara dua kategori")