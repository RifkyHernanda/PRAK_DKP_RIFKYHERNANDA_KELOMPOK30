class contoh_method:
    #init method
  def __init__(self, praktikan1, praktikan2):
    self.praktikan1 = praktikan1
    self.praktikan2 = praktikan2

    #self parameter
  def mulai(self):
    print(f"Selamat Datang di Percobaan 2 {self.praktikan1} dan {self.praktikan2}")

    #method dengan parameter
  def selesai(self, waktu):
    print("Percobaan akan selesai dalam :")
    while waktu > 0:
      print(waktu)
      waktu -= 1


p1 = contoh_method("Rifky","Hernanda")
p1.mulai()
p1.selesai(3)
