import tkinter as tk
import math
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

def kup_hacim():
    root.destroy()

    global uzunluk
    global root1

    root1 = tk.Tk()
    root1.title("Küpün Hacmi")
    root1.geometry("500x500+50+50")
    root1.resizable(False, False)

    kup = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/cube.png"))
    image = tk.Label(root1, image = kup)
    image.pack()

    uzunlukLabel = tk.Label(root1, text = "Uzunluk:")
    uzunlukLabel.pack()

    uzunluk = tk.Entry(root1, width = 50)
    uzunluk.pack()

    button = tk.Button(root1, text = "Hesapla", command = hesaplakup)
    button.pack()
   
    root.mainloop()

def hesaplakup():
    try:
        t1 = int(uzunluk.get())
        hacim = t1 ** 3
    
        sonuc = tk.Label(root1, text = hacim)
        sonuc.pack()

    except ValueError:
        print("Aptal")
    

def dikprizmahacim():
    root.destroy()

    global uzunluk1
    global uzunluk2
    global uzunluk3
    global root1
    
    root1 = tk.Tk()
    root1.title("Dik Prizmanın Hacmi")
    root1.geometry("500x500+50+50")
    root1.resizable(False, False)

    dikdortgenlerprizmasi = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/dikdörtgenlerprizması.png"))
    image = tk.Label(root1, image = dikdortgenlerprizmasi)
    image.pack()

    uzunluk1Label = tk.Label(root1, text = "1. Uzunluk:")
    uzunluk1Label.pack()

    uzunluk1 = tk.Entry(root1, width = 50)
    uzunluk1.pack()

    uzunluk2Label = tk.Label(root1, text = "2. Uzunluk:")
    uzunluk2Label.pack()

    uzunluk2 = tk.Entry(root1, width = 50)
    uzunluk2.pack()

    uzunluk3Label = tk.Label(root1, text = "3. Uzunluk:")
    uzunluk3Label.pack()

    uzunluk3 = tk.Entry(root1, width = 50)
    uzunluk3.pack()

    button = tk.Button(root1, text = "Hesapla", command = hesapladik)
    button.pack()
    
    root.mainloop()

def hesapladik():
    try:
        t1 = int(uzunluk1.get())
        t2 = int(uzunluk2.get())
        t3 = int(uzunluk3.get())

        hacim = t1 * t2 * t3
    
        sonuc = tk.Label(root1, text = hacim)
        sonuc.pack()

    except ValueError:
        print("Aptal")    

def silindirhacmi():
    root.destroy()

    global uzunluk
    global yaricap
    global root1
    global pi

    pi = math.pi
    
    root1 = tk.Tk()
    root1.title("Silindirin Hacmi")
    root1.geometry("500x500+50+50")
    root1.resizable(False, False)
    
    silindir = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/silindir.png"))
    image = tk.Label(root1, image = silindir)
    image.pack()

    uzunlukLabel = tk.Label(root1, text = "Uzunluk:")
    uzunlukLabel.pack()

    uzunluk = tk.Entry(root1, width = 50)
    uzunluk.pack()

    yaricapLabel = tk.Label(root1, text = "Yarıçap:")
    yaricapLabel.pack()

    yaricap = tk.Entry(root1, width = 50)
    yaricap.pack()

    button = tk.Button(root1, text = "Hesapla", command = hesaplasilindir)
    button.pack()
    
    root.mainloop()

def hesaplasilindir():
    try:
        t1 = int(uzunluk.get())
        t2 = int(yaricap.get())

        hacim = t1 * t2 * t2 * pi
            
        sonuc = tk.Label(root1, text = hacim)
        sonuc.pack()

    except ValueError:
        print("Aptal")
        
def konihacmi():
    root.destroy()

    global uzunluk
    global root1
    global yaricap
    global pi

    pi = math.pi
    
    root1 = tk.Tk()
    root1.title("Koninin Hacmi")
    root1.geometry("500x500+50+50")
    root1.resizable(False, False)
    
    koni = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/koni.jpg"))
    image = tk.Label(root1, image = koni)
    image.pack()

    uzunlukLabel = tk.Label(root1, text = "Uzunluk:")
    uzunlukLabel.pack()

    uzunluk = tk.Entry(root1, width = 50)
    uzunluk.pack()

    yaricapLabel = tk.Label(root1, text = "Yarıçap:")
    yaricapLabel.pack()

    yaricap = tk.Entry(root1, width = 50)
    yaricap.pack()

    button = tk.Button(root1, text = "Hesapla", command = hesaplakoni)
    button.pack()
        
    root.mainloop()

def hesaplakoni():
    try:
        t1 = int(uzunluk.get())
        t2 = int(yaricap.get())

        hacim = t2 * t2 * t1 * pi * 1 / 3
            
        sonuc = tk.Label(root1, text = hacim)
        sonuc.pack()

    except ValueError:
        print("Aptal")

def kareprizmahacmi():
    root.destroy()

    global kuzunluk
    global uzunluk
    global root1
    
    root1 = tk.Tk()
    root1.title("Küpün Hacmi")
    root1.geometry("500x500+50+50")
    root1.resizable(False, False)
    
    karepiramit = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/karepiramit.png"))
    image = tk.Label(root1, image = karepiramit)
    image.pack()

    kuzunlukLabel = tk.Label(root1, text = "Uzunluk(h):")
    kuzunlukLabel.pack()

    kuzunluk = tk.Entry(root1, width = 50)
    kuzunluk.pack()

    uzunlukLabel = tk.Label(root1, text = "Uzunluk:")
    uzunlukLabel.pack()

    uzunluk = tk.Entry(root1, width = 50)
    uzunluk.pack()

    button = tk.Button(root1, text = "Hesapla", command = hesaplakare)
    button.pack()
    
    root.mainloop()

def hesaplakare():
    try:
        t1 = int(kuzunluk.get())
        t2 = int(uzunluk.get())

        hacim = t2 * t2 * t1 * 1 / 3
            
        sonuc = tk.Label(root1, text = hacim)
        sonuc.pack()

    except ValueError:
        print("Aptal")


def kurehacmi():
    root.destroy()

    global yaricap
    global root1
    global pi

    pi = math.pi
    
    root1 = tk.Tk()
    root1.title("Kürenin Hacmi")
    root1.geometry("500x500+50+50")
    root1.resizable(False, False)
    
    kure = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/küre.png"))
    image = tk.Label(root1, image = kure)
    image.pack()

    yaricapLabel = tk.Label(root1, text = "Yarıçap:")
    yaricapLabel.pack()

    yaricap = tk.Entry(root1, width = 50)
    yaricap.pack()

    button = tk.Button(root1, text = "Hesapla", command = hesaplakure)
    button.pack()
    
    
    root.mainloop()

def hesaplakure():
    try:
        t2 = int(yaricap.get())

        hacim = t2 * t2 * t2 * 4 / 3 * pi
            
        sonuc = tk.Label(root1, text = hacim)
        sonuc.pack()

    except ValueError:
        print("Aptal")

root = tk.Tk()
root.title("Hacim Hesaplayıcı")

root.geometry("1800x600+50+50")
root.resizable(False, False)

anasayfa = tk.Label(root, text='Bir şekil seç', font = ("Times New Roman", 20))
anasayfa.pack()

kup = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/cube.png"))
dikdortgenlerprizmasi = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/dikdörtgenlerprizması.png"))
silindir = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/silindir.png"))
koni = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/koni.jpg"))
karepiramit = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/karepiramit.png"))
kure = ImageTk.PhotoImage(Image.open("D:/YAZILIM/Python/Tkinter/küre.png"))

kupButton = ttk.Button(root, image = kup, compound = tk.LEFT, command = kup_hacim)
kupButton.pack(padx=0, pady=0, expand=True, side = tk.LEFT)

dikdortButton = ttk.Button(root, image = dikdortgenlerprizmasi, compound = tk.LEFT, command = dikprizmahacim)
dikdortButton.pack(padx=0, pady=1, expand=True, side = tk.LEFT)

silindirButton = ttk.Button(root, image = silindir, compound = tk.LEFT, command = silindirhacmi)
silindirButton.pack(padx=0, pady=2, expand=True, side = tk.LEFT)

koniButton = ttk.Button(root, image = koni, compound = tk.LEFT, command = konihacmi)
koniButton.pack(padx = 1, pady = 0, expand = True, side = tk.LEFT)

karepiramitButton = ttk.Button(root, image = karepiramit, compound = tk.LEFT, command = kareprizmahacmi)
karepiramitButton.pack(padx = 1, pady = 1, expand = True, side = tk.LEFT)

kureButton = ttk.Button(root, image = kure, compound = tk.LEFT, command = kurehacmi)
kureButton.pack(padx = 1, pady = 2, expand = True, side = tk.LEFT)


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()


root.mainloop()


