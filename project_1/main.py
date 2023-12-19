import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import datetime
import csv

n = int(input("Podaj liczbę n: "))

def ex_1():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass

def ex_2():
    with open("liczby.txt", "w") as plik:
        for i in range(n):
            liczba = random.randint(1, 100)  # losowa liczba z zakresu 1-100
            plik.write(str(liczba) + "\n")  # zapisz liczbę do pliku w nowej linii
    pass

def ex_3():
    def wczytaj_liczby():
        lista = []  # pusta lista na liczby
        with open("liczby.txt", "r") as plik:
            for linia in plik:
                liczba = int(linia)  # zamień napis na liczbę
                lista.append(liczba)  # dodaj liczbę do listy
        return lista  # zwróć listę

    def srednia(lista):
        suma = 0  # zmienna na sumę liczb
        n = len(lista)  # ilosc liczb w liście
        for liczba in lista:
            suma += liczba  # dodaj liczbę do sumy
        return suma / n

    def odchylenie(lista):
        sred = srednia(lista)  # obliczanie średniej
        suma = 0  # zmienna na sumę kwadratów różnic
        n = len(lista)  # ilosc liczb w liście
        for liczba in lista:
            roznica = liczba - sred  # różnica między liczbą a średnią
            suma += roznica ** 2  # dodanie kwadratu różnicy do sumy
        return math.sqrt(suma / n)  # pierwiastek z wariancji

    def maksimum(lista):
        maks = lista[0]  # zmienna na maksymalną liczbę
        for liczba in lista:
            if liczba > maks:  # jeśli liczba jest większa od maksimum
                maks = liczba  # ustaw nowe maksimum
        return maks

    def minimum(lista):
        mini = lista[0]  # zmienna na minimalną liczbę
        for liczba in lista:
            if liczba < mini:  # jeśli liczba jest mniejsza od minimum
                mini = liczba  # ustaw nowe minimum
        return mini

    def sortuj(lista):
        posortowana = []  # pusta lista na posortowane liczby
        while lista:
            mini = minimum(lista)  # najmniejsza liczba
            lista.remove(mini)  # usuń liczbe z listy
            posortowana.append(mini)  # dodaj liczbe do listy posortowanej
        return posortowana[::-1]  # odwróć kolejność i zwróć listę

    liczby = wczytaj_liczby()  # wczytaj liczby z pliku
    print("Liczby wczytane z pliku:", liczby)  # wyświetl liczby
    print("Średnia:", srednia(liczby))  # wyświetl średnią
    print("Odchylenie standardowe:", odchylenie(liczby))  # wyświetl odchylenie
    print("Maksimum:", maksimum(liczby))  # wyświetl maksimum
    print("Minimum:", minimum(liczby))  # wyświetl minimum
    print("Liczby posortowane malejąco:", sortuj(liczby))  # wyświetl posortowane liczby
    pass

def ex_4(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (ex_4(n - 1) + ex_4(n - 2))

def ex_5():
    def generuj_fibonacci(n):
        lista = []  # pusta lista na liczby Fibonacciego
        for i in range(n):
            liczba = ex_4(i)  # oblicz i-tą liczbę Fibonacciego
            lista.append(liczba)  # dodaj ją do listy
        return lista  # zwróć listę

    def wykres_fibonacci(n):
        liczby = generuj_fibonacci(n)  # wygeneruj n liczb Fibonacciego
        plt.plot(liczby)  # wykres
        plt.title("Ciąg Fibonacciego")  # tytuł
        plt.xlabel("Numer wyrazu")  # tekst osi x
        plt.ylabel("Wartość wyrazu")  # tekst osi y
        plt.show()  # pokaż wykres
    wykres_fibonacci(n)
    pass

def ex_6():
    def make_dict(n):
        dict = {}
        for x in range(1, n + 1):
            dict[x] = x ** 2
        return dict

    dict = make_dict(n)
    print(dict)
    return dict
    pass
def ex_7():

    def suma_wartosci(dict):
        suma = 0  # suma wartości
        for x in dict.values():  # dla każdej wartości w słowniku
            suma += x  # dodawanie wartości do sumy
        return suma  # zwróć sumę

    dict = {}
    dict = ex_6()
    print("Suma wartości:", suma_wartosci(dict))
    pass

def ex_8():
    def zapisz_losowe_dane():
        i = 0
        for i in range(10):  # dla każdego z 10 plików
            nazwa = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")  # utwórz nazwę pliku z datą i godziną
            with open(nazwa, "wb") as plik:  # otwórz plik w trybie binarnym
                dane = random.getrandbits(100)  # wygeneruj 100 losowych bitów
                plik.write(dane.to_bytes(13, "big"))  # zapisz dane do pliku jako bajty
            time.sleep(0.1)
    zapisz_losowe_dane()
    pass

def ex_9():

    def csv_read(name):
        data = np.loadtxt(name, delimiter=",", skiprows=1, dtype=float)
        return data

    def position(data):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)  # utwórz trzy wykresy ułożone pionowo
        ax1.plot(data[:, 0], data[:, 1],
                 color="red")  # wykres pozycji x w osi y, kolor czerwony
        ax1.set_ylabel("pos_x")  # ustaw tekst osi y
        ax2.plot(data[:, 0], data[:, 2],
                 color="green")  # wykres pozycji y w osi y,  kolor zielony
        ax2.set_ylabel("pos_y")  # ustaw tekst osi y
        ax3.plot(data[:, 0], data[:, 3],
                 color="blue")  # wykres pozycji z w osi y, kolor niebieski
        ax3.set_ylabel("pos_z")  # ustaw tekst osi y
        ax3.set_xlabel("timestamp")  # ustaw tekst osi x
        ax1.tick_params(direction='in', axis='both') # parametry osi
        ax1.set_ylim(-40, 40) # limity osi y
        ax2.tick_params(direction='in', axis='both') # parametry osi
        ax2.set_ylim(17, 23) # limity osi y
        ax3.tick_params(direction='in', axis='both') # parametry osi
        ax3.set_ylim(0.5, 3.5) # limity osi y
        plt.suptitle("Pozycje w osiach x, y i z")  # tytuł wykresu
        plt.show()

    def avg_position(data):
        avg_x = np.average(data[:, 1])  # oblicz średnią pozycje x
        avg_y = np.average(data[:, 2])  # oblicz średnią pozycje y
        avg_z = np.average(data[:, 3])  # oblicz średnią pozycje z
        print("Średnia pozycja x:", avg_x)  # wypisz średnią pozycję x
        print("Średnia pozycja y:", avg_y)  # wypisz średnią pozycję y
        print("Średnia pozycja z:", avg_z)  # wypisz średnią pozycję z

    def speed(data):
        speed = np.sqrt(data[:, 4] ** 2 + data[:, 5] ** 2 + data[:, 6] ** 2)  # oblicz szybkość z wektora prędkości
        np.savetxt("velocity.csv", speed, newline="\n", fmt="%.2f")  # zapisz szybkość do pliku

    data = csv_read("reference_trajectory.csv") # odczyt danych
    position(data)  # wykresy
    avg_position(data)  # średnie
    speed(data)  # szybkość
    pass


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
