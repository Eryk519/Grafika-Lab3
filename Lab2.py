from PIL import Image
import numpy as np

obraz= Image.open("obraz.bmp")
obraz.show()
print("tryb", obraz.mode)
print("format", obraz.format)
print("rozmiar", obraz.size)

t_obraz = np.asarray(obraz)
print("typ danych tablicy", t_obraz.dtype)
print("rozmiar tablicy", t_obraz.shape)
print("***************************************")


def wstaw_obraz(t_obraz,wsp: int,h_m: int,w_m: int):
    h0, w0 = t_obraz.shape
    print(h0, w0)
    t = (int(wsp * h0), int(wsp * w0))
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(int(h_m), min(int(wsp*h0), int(h_m) + h0)):
        for j in range(int(w_m), min(int(wsp*w0), int(w_m) + w0)):
            tab[i][j] = t_obraz[i - int(h_m)][j - int(w_m)]
    tab = tab.astype(bool)
    obraz_wstawiany = Image.fromarray(tab)
    return obraz_wstawiany

obraz_wstawiany = wstaw_obraz(t_obraz,2,60,70)
obraz_wstawiany.show()
obraz_wstawiany.save("obrazprzyciety.bmp")

def rysuj_pasy_poziome(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    poziom = Image.fromarray(tab)
    poziom.show()
    poziom.save("poziom.bmp")
rysuj_pasy_poziome(400, 630, 9)

def rysuj_ramke(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    ilosc = int(min(w, h) / grub)
    for j in range(ilosc + 1):
        if j % 2 == 0:
            n = h - j*grub
            p = w - j*grub
            tab[j*grub:n, j*grub:p] = 1
        else:
            n = h - j*grub
            p = w - j*grub
            tab[j * grub:n, j * grub:p] = 0
    return tab * 255

ramka = rysuj_ramke(240, 120, 8)
ramka1 = Image.fromarray(ramka)
ramka1.save("ramkanaprzemian.bmp")
ramka1.show()
