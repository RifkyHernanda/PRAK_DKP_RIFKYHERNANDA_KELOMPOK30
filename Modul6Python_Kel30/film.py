class film(object):
    """description of class"""
    __judul = ""
    __genre = ["", ""]
    __rate = 0.0
    __tahun = 0
 
    def __init__(self, judul, genre, rate, tahun):
        self.__judul = judul
        self.__genre = genre
        self.__rate = rate
        self.__tahun = tahun
        pass
 
    def setGenre(self, genreBaru):
        self.__genre = genreBaru
        pass
 
    def setRate(self, rateBaru):
        self.__rate = rateBaru
        pass	
 
    def getJudul(self):
        return self.__judul
 
    def getGenre(self):
        for item in self.__genre:
            print(item)
        pass
 
    def getRate(self):
        return self.__rate
 
    def getTahun(self):
        return self.__tahun
