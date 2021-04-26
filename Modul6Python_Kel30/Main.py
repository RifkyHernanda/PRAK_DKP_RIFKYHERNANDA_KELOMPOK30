from film import film
 
avengers = film("The Avengers", ["Action", "Fantasy"], 7.9, 2012)

print("Kelompok 30")
print("-- Tahun 2013 --")
print("Judul : " + avengers.getJudul())
print("Genre : ")
avengers.getGenre()
print("Rate : " + str(avengers.getRate()))
print("Tahun : " + str(avengers.getTahun()))
 
avengers.setGenre(["Action", "Fiction", "Alien"])
avengers.setRate(8.4)
 
print("\n-- Tahun 2018 --")
print("Judul : " + avengers.getJudul())
print("Genre : ")
avengers.getGenre()
print("Rate : " + str(avengers.getRate()))
print("Tahun : " + str(avengers.getTahun()))
