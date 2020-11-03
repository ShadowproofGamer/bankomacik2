#import z pliku
plik = open("banknoty.txt")
dane = plik.read().split()
#import danych do słownika i tabeli wartości
ilosc = []
wartosci = []
tabela = {}
for i in range(0, len(dane), 2):
    tabela[dane[i]] = int(dane[i+1])
    wartosci.append(int(dane[i]))
    ilosc.append(int(dane[i+1]))

plik.close()
plik = open("banknoty.txt", 'w')
wartosci.reverse()

def zapis(banknoty, ilosci):
    for i in range(len(banknoty)):
        plik.write(str(banknoty[i])+'\t'+str(ilosci[i])+'\n')

def slownik_sync(klucz, wartosc, tryb):
    wartosci.reverse()
    if tryb=='ustaw':
        tabela.update({klucz:wartosc})
        ilosc[wartosci.index(int(klucz))] = wartosc
    if tryb=='zaktualizuj':
        tabela.update({klucz:tabela[klucz]-wartosc})
        ilosc[wartosci.index(int(klucz))] -= wartosc
    #print('banknot: '+klucz+' wartosci: '+str(ilosc[wartosci.index(int(klucz))]))
    wartosci.reverse()


def wyplata(pieniodze, banknot, ilosc):
    wyplacone = {}
    for i in banknot:
        if(pieniodze==0):
            break
        dostepne = ilosc[str(i)]
        #print(dostepne)
        #print(i)
        if int(pieniodze/i) > dostepne:
            wyplacone[str(i)] = dostepne
            pieniodze -= i*dostepne
            slownik_sync(str(i), 0, 'ustaw')
        else:
            wyplacone[str(i)] = int(pieniodze/i)
            pieniodze -= i * wyplacone[str(i)]
            slownik_sync(str(i),  wyplacone[str(i)], 'zaktualizuj')
    return wyplacone


print('wyplacone ' + str(wyplata(880, wartosci, tabela)))
wartosci.reverse()
zapis(wartosci, ilosc)
