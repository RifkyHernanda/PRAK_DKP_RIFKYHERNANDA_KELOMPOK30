class CheckIP(object):
    #def __init__(self, IP):
     #   self.IP = IP
    indeksOktet1, indeksOktet2, indeksOktet3, indeksSlash = 0,0,0,0
    Oktet1, Oktet2, Oktet3, Oktet4, IP, Slash = "","","","","",""
    def __init__(self, IP , indeksOktet1, indeksOktet2, indeksOktet3, indeksSlash, Oktet1, Oktet2, Oktet3, Oktet4, Slash):
        self.indeksOktet1 = indeksOktet1
        self.indeksOktet2 = indeksOktet2
        self.indeksOktet3 = indeksOktet3
        self.Oktet1 = Oktet1
        self.Oktet2 = Oktet2
        self.Oktet3 = Oktet3
        self.Oktet4 = Oktet4
        self.IP     = IP
        self.indeksSlash = indeksSlash
        self.Slash = Slash
        pass
    def setIP(self, IP):
        self.IP = IP
        pass
    def ngecekIP(self):
        for i in range(len(self.IP)):
            if str(self.IP[i:i+1]) == ".":
                if self.indeksOktet1 == 0:
                    self.indeksOktet1 = i
                elif self.indeksOktet2 == 0:
                    self.indeksOktet2 = i
                elif self.indeksOktet3 == 0:
                    self.indeksOktet3 = i
            if str(self.IP[i:i+1]) == "/":
                self.indeksSlash = i
        if self.indeksSlash == 0:
            self.Oktet1 = self.IP[0:self.indeksOktet1]
            self.Oktet2 = self.IP[self.indeksOktet1+1:self.indeksOktet2]
            self.Oktet3 = self.IP[self.indeksOktet2+1:self.indeksOktet3]
            self.Oktet4 = self.IP[self.indeksOktet3+1:]
        else:
            self.Oktet1 = self.IP[0:self.indeksOktet1]
            self.Oktet2 = self.IP[self.indeksOktet1+1:self.indeksOktet2]
            self.Oktet3 = self.IP[self.indeksOktet2+1:self.indeksOktet3]
            self.Oktet4 = self.IP[self.indeksOktet3+1:self.indeksSlash]
            self.Slash = self.IP[self.indeksSlash+1:]
        print(self.indeksOktet1, self.indeksOktet2, self.indeksOktet3, self.indeksSlash)
        print(self.Oktet1, self.Oktet2, self.Oktet3, self.Oktet4, self.Slash)
    def getOktet1(self):
        return self.Oktet1
    def getOktet2(self):
        return self.Oktet2
    def getOktet3(self):
        return self.Oktet3
    def getOktet4(self):
        return self.Oktet4
    def getIndeksOktet3(self):
        return self.indeksOktet3
    def getSlash(self):
        return self.Slash
    def getIndeksSlash(self):
        return self.indeksSlash
    def setOktet(self, bersihin):
        self.Oktet1 = ""
        self.Oktet2 = ""
        self.Oktet3 = ""
        self.Oktet4 = ""
        self.Slash  = ""
        self.indeksOktet1 = 0
        self.indeksOktet2 = 0
        self.indeksOktet3 = 0
        self.indeksSlash = 0
        pass