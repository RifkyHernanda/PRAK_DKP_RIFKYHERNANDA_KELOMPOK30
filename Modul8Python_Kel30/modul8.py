from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

def submit():
    perkenalan=""
    if len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI NAMA")
        return
    if radio.get()== 0:
        messagebox.showerror("Error","BELUM MEMILIH JENIS KELAMIN")
        return
    elif radio.get() == 1:
        perkenalan="Mas "
    elif radio.get() == 2:
        perkenalan="Mbak "
    if strhobi.get() == 'Hobi aku ...':
        messagebox.showerror("Error","BELUM MEMILIH HOBI")
        return
    pesan = "Halo " + perkenalan + stringnama.get() + " yang hobinya " + strhobi.get() + "!!!"
    messagebox.showinfo("Greeting", pesan)
    
  
top = Tk()  
top.geometry("300x200")
top.title("Python GUI")

#creating label  
lbnama = Label(top, text = "Nama\t:").place(x = 30,y = 10)    
lbjk = Label(text = "Gender\t:").place(x = 30, y=40)
lbhb = Label(text = "Hobi\t:").place(x=30, y=110)

#create input  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama).place(x = 110, y = 10)  

#create radio
radio = IntVar()
R1 = Radiobutton(top, text="Pria", variable=radio, value=1).place(x=105, y=40)  
R2 = Radiobutton(top, text="Wanita", variable=radio, value=2).place(x=105, y=60)  
R3 = Radiobutton(top, text="Tidak ingin memberitahu", variable=radio, value=3).place(x=105, y=80)  

#create combobox
strhobi = StringVar(value='Hobi aku ...') 
Cb1 = ttk.Combobox(top, width = 17, textvariable = strhobi, state="readonly")
Cb1.place(x=110, y=110)

# Adding combobox drop down list 
Cb1['values'] = ('Sepak Bola',
                 'Basket',
                 'Renang',
                 'Mancing') 

#create button
btn1 = Button(top, command = submit, text="SUBMIT").place(x=120,y=150)

top.mainloop()
