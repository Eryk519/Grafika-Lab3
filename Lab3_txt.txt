from PIL import Image
import numpy as np

#Zad3
def koloruj_obraz(obraz,zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    kolor_r = 0
    kolor_g = 0
    kolor_b = 0
    for i in range(h):
        for j in range(w):
            kolor_r = kolor_r + zmiana_koloru_r
            kolor_g = kolor_g + zmiana_koloru_g
            kolor_b = kolor_b + zmiana_koloru_b
            if t_obraz[i, j] == False:
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
            else:
                tab[i, j] = [255, 255, 255]
    return tab

inicjaly = Image.open("inicjaly.bmp")
obraz2 = Image.fromarray(koloruj_obraz(inicjaly, 4,6,8))
obraz2.show()
obraz2.save("inicjalywkolorze.bmp")

#Zad1
def rysuj_ramke(w, h, dzielnik,zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    ilosc = int(min(w, h) / grub)
    kolor_r = 0
    kolor_g = 0
    kolor_b = 0
    for j in range(ilosc + 1):
        if j % 2 == 0:
            n = h - j*grub
            p = w - j*grub
            tab[j*grub:n, j*grub:p] = [kolor_r, kolor_g, kolor_b]
            kolor_r = kolor_r + zmiana_koloru_r
            kolor_g = kolor_g + zmiana_koloru_g
            kolor_b = kolor_b + zmiana_koloru_b
        else:
            n = h - j*grub
            p = w - j*grub
            tab[j * grub:n, j * grub:p] = [kolor_r, kolor_g, kolor_b]
            kolor_r = kolor_r + zmiana_koloru_r
            kolor_g = kolor_g + zmiana_koloru_g
            kolor_b = kolor_b + zmiana_koloru_b
    return tab * 255

ramka = rysuj_ramke(240, 120, 8, 100, 100, 100)
ramka1 = Image.fromarray(ramka)
ramka1.save("ramkanaprzemian.bmp")
ramka1.show()


#Zad2
def rysuj_pasy_poziome(w, h, dzielnik,zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    kolor_r = 0
    kolor_g = 0
    kolor_b = 0
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = tab[j, i] = [kolor_r, kolor_g, kolor_b]
        kolor_r = kolor_r + zmiana_koloru_r
        kolor_g = kolor_g + zmiana_koloru_g
        kolor_b = kolor_b + zmiana_koloru_b
    tab = tab * 255
    poziom = Image.fromarray(tab)
    poziom.show()
    poziom.save("poziom.bmp")
rysuj_pasy_poziome(200, 630, 9, 248, 244, 240)