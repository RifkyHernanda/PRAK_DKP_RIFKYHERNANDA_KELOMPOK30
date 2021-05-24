from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 
from ipconf import CheckIP
Ipconfig = CheckIP("",0,0,0,0,"","","","","")
def submit():
    clear()
    InputIP = stringnama.get()
    InputCIDR = stringCIDR.get()
    Ipconfig.setIP(str(InputIP))
    Ipconfig.ngecekIP()
    indeks3 = Ipconfig.getIndeksOktet3()
    if len(str(InputIP))> indeks3+8 or len(str(InputIP))>18:
        messagebox("Warning", "IP nya salah")
    else:
        Oktet1 = Ipconfig.getOktet1()
        Oktet2 = Ipconfig.getOktet2()
        Oktet3 = Ipconfig.getOktet3()
        Oktet4 = Ipconfig.getOktet4()
        if int(Oktet1)>0 and int(Oktet1)<=127:
            Kel  = "A"
            HoID = Oktet1
            NeID = Oktet2 + "." + Oktet3 + "." + Oktet4
        elif int(Oktet1)>127 and int(Oktet1)<=191:
            Kel  = "B"
            HoID = Oktet1 + "." + Oktet2  
            NeID = Oktet3 + "." + Oktet4
        elif int(Oktet1)>=192 and int(Oktet1)<=254:
            Kel  = "C"
            HoID = Oktet1 + "." + Oktet2 + "." + Oktet3
            NeID = Oktet4 
        else:
            messagebox("Warning", "IP nya salah")
        Slash = 0
        Subnet = ""
        if stringCIDR.get() != 0 :
            Slash = int(stringCIDR.get())
            SisaBagi = Slash%8
            CIDR = {
                0: "0",
                1: "128",
                2: "192",
                3: "224",
                4: "240",
                5: "248",
                6: "252",
                7: "254",
            }
            lastsub = CIDR.setdefault(SisaBagi)
            IPbroadcast = ''
            IPhost = ''
            IPrange = ''
            host= 2**(8-SisaBagi)
            berapakali = int(Oktet4)//host
            if Slash>=8 and Slash<=15:
                Subnet = "255."+lastsub+".0.0"
                IPhost = Oktet1+'.' + str(host*berapakali)+'.0.0'
                IPbroadcast = Oktet1+'.' + str((host*(berapakali+1))-1)+'.255.255'
                IPrange = Oktet1+'.' + str((host*berapakali)+1)+'.0.0'+'  -  ' + Oktet1+'.' + str((host*(berapakali+1))-1)+'.255.254'
            elif Slash>=16 and Slash<=23:
                Subnet = "255.255."+lastsub+".0"
                IPhost = Oktet1+'.'+Oktet2+'.' + str(host*berapakali)+'.0'
                IPbroadcast = Oktet1+'.'+Oktet2+'.' + str((host*(berapakali+1))-1)+'.255'
                IPrange = Oktet1+'.'+Oktet2+'.' + str((host*berapakali)+1)+'.0'+'  -  ' + Oktet1+'.'+Oktet2+'.' + str((host*(berapakali+1))-1)+'.254'
            elif Slash>=24 and Slash<=31:
                Subnet = "255.255.255."+lastsub
                IPhost = Oktet1+'.'+Oktet2+'.' +Oktet3+'.'+ str(host*berapakali)
                IPbroadcast = Oktet1+'.'+Oktet2+'.'+Oktet3+'.' + str((host*(berapakali+1))-1)
                IPrange = Oktet1+'.'+Oktet2+'.'+Oktet3+'.' + str((host*berapakali)+1)+'  -  ' + Oktet1+'.'+Oktet2+'.'+Oktet3+'.' + str((host*(berapakali+1))-2)
        print(IPhost)
        print(IPbroadcast)
        print(IPrange)
        lbIP = Label(top, text = "IP\t:",background="Deep Sky Blue2").place(x = 30,y = 10)   
        lbKelas = Label(top, text = "Kelas\t: "+Kel,background="Deep Sky Blue2").place(x = 30,y = 40)    
        lbHost = Label(text = "Host ID\t: "+HoID,background="Deep Sky Blue2").place(x = 30, y=70)
        lbNetwork = Label(text = "Net ID\t: "+NeID,background="Deep Sky Blue2").place(x=30, y=100)
        lbOktet1 = Label(text = "Oktet1\t: "+Oktet1,background="Deep Sky Blue2").place(x=30, y=130)
        lbOktet2 = Label(text = "Oktet2\t: "+Oktet2,background="Deep Sky Blue2").place(x=30, y=160)
        lbOktet3 = Label(text = "Oktet3\t: "+Oktet3,background="Deep Sky Blue2").place(x=175, y=130)
        lbOktet4 = Label(text = "Oktet4\t: "+Oktet4,background="Deep Sky Blue2").place(x=175, y=160)
        lbSlash = Label(text = "Subnet\t: "+Subnet,background="Deep Sky Blue2").place(x=30, y=190)
        lbIPhost = Label(text = "IP Host\t\t: "+IPhost,background="Deep Sky Blue2").place(x=30, y=220)
        lbIPBroadcast = Label(text = "IP Broadcast\t: "+IPbroadcast,background="Deep Sky Blue2").place(x=30, y=250)
        lbIPRange = Label(text = "IP Range\t\t: "+IPrange,background="Deep Sky Blue2").place(x=30, y=280)
def clear():
    lbIP = Label(top, text = "IP\t:",background="Deep Sky Blue2").place(x = 30,y = 10)   
    lbKelas = Label(top, text = "Kelas\t:                             ",background="Deep Sky Blue2").place(x = 30,y = 40)    
    lbHost = Label(text = "Host ID\t:                             ",background="Deep Sky Blue2").place(x = 30, y=70)
    lbNetwork = Label(text = "Net ID\t:                             ",background="Deep Sky Blue2").place(x=30, y=100)
    lbOktet1 = Label(text = "Oktet1\t:                             ",background="Deep Sky Blue2").place(x=30, y=130)
    lbOktet2 = Label(text = "Oktet2\t:                             ",background="Deep Sky Blue2").place(x=30, y=160)
    lbOktet3 = Label(text = "Oktet3\t:                             ",background="Deep Sky Blue2").place(x=175, y=130)
    lbOktet4 = Label(text = "Oktet4\t:                             ",background="Deep Sky Blue2").place(x=175, y=160)
    lbSlash = Label(text = "Subnet\t:                              ",background="Deep Sky Blue2").place(x=30, y=190)
    lbIPhost = Label(text = "IP Host\t\t:                                                                  ",background="Deep Sky Blue2").place(x=30, y=220)
    lbIPBroadcast = Label(text = "IP Broadcast\t:                                                          ",background="Deep Sky Blue2").place(x=30, y=250)
    lbIPRange = Label(text = "IP Range\t\t:                                                                                               ",background="Deep Sky Blue2").place(x=30, y=280)
    Ipconfig.setOktet(0)
top = Tk()  
top.geometry("350x450")
top.configure(background='Deep Sky Blue2')
top.title("Kalkulator IP")

#creating label  
lbIP = Label(top, text = "IP\t:",background="Deep Sky Blue2").place(x = 30,y = 10)
lbCIDR = Label(top, text = '/', background="Deep Sky Blue2").place(x= 215, y = 10)   
lbKelas = Label(top, text = "Kelas\t:",background="Deep Sky Blue2").place(x = 30,y = 40)    
lbHost = Label(text = "Host ID\t:",background="Deep Sky Blue2").place(x = 30, y=70)
lbNetwork = Label(text = "Net ID\t:",background="Deep Sky Blue2").place(x=30, y=100)
lbOktet1 = Label(text = "Oktet1\t:",background="Deep Sky Blue2").place(x=30, y=130)
lbOktet2 = Label(text = "Oktet2\t:",background="Deep Sky Blue2").place(x=30, y=160)
lbOktet3 = Label(text = "Oktet3\t:",background="Deep Sky Blue2").place(x=175, y=130)
lbOktet4 = Label(text = "Oktet4\t:",background="Deep Sky Blue2").place(x=175, y=160)
lbSlash = Label(text = "Subnet\t: ",background="Deep Sky Blue2").place(x=30, y=190)
lbIPhost = Label(text = "IP Host\t\t: ",background="Deep Sky Blue2").place(x=30, y=220)
lbIPBroadcast = Label(text = "IP Broadcast\t: ",background="Deep Sky Blue2").place(x=30, y=250)
lbIPRange = Label(text = "IP Range\t\t: ",background="Deep Sky Blue2").place(x=30, y=280)
#create input  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama, ).place(x = 90, y = 10)  
stringCIDR = StringVar(value='24')
Cb1 = ttk.Combobox(top,width=5, textvariable=stringCIDR,state="readonly")
Cb1.place(x=225, y = 10)
Cb1['values']=('8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
#iCIDR = Entry(top,width = 5, textvariable=stringCIDR, ).place(x = 225, y = 10) 
#create button
btn1 = Button(top, command = submit, text="SUBMIT").place(x=100,y=340)
btn2 = Button(top, command = clear, text="CLEAR").place(x=170,y=340)
top.mainloop()
