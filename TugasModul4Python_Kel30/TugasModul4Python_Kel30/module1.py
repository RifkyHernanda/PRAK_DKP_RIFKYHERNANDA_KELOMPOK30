class tugasmodul4:
  def PerkenalanKelompok(nomorkel, shift):
    print(f"Kelompok {nomorkel} shift {shift}")
  def NamaAnggota(*perkenalan):
    n = 0
    for nama in perkenalan:
        n+=1
        print(f"{n}. ",nama)
  def printgaris(jumlah):
      if jumlah >=1 :
        garis = ""
        while jumlah>0:
            garis = garis + "="
            jumlah-=1
        print(garis)
      else:
        print("=============================================================================")
        print("===========================Nota Kasir Sederhana==============================")
        print("=============================================================================")
          

