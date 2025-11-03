import random  # importa moduli necessari
from Transazione import Transazione  # importa moduli necessari

# il contocorrente che gestisce le varie transazioni e il saldo
class ContoCorrente:  # definisce una classe
    def __init__(self):  # definisce una funzione o metodo
        self.iban = random.randint(10**10, 10**11 - 1)  # assegna un valore a una variabile
        self.saldo = 0  # assegna un valore a una variabile
        self.lista_movimenti = []  # assegna un valore a una variabile
    def deposita(self, importo):  # importa moduli necessari
        if importo > 0:  # importa moduli necessari
            self.saldo += importo  # importa moduli necessari
            transazione = Transazione("Versamento", importo, self.saldo)  # importa moduli necessari
            self.lista_movimenti.append(transazione)  # accede a un attributo o metodo
    def preleva(self, importo):  # importa moduli necessari
        if importo <= self.saldo and importo > 0:  # importa moduli necessari
            self.saldo -= importo  # importa moduli necessari
            transazione = Transazione("Prelievo", importo, self.saldo)  # importa moduli necessari
            self.lista_movimenti.append(transazione)  # accede a un attributo o metodo
        else:  # esegue in caso contrario
            print("Fondi insufficienti")  # stampa un messaggio
    def get_saldo(self):  # definisce una funzione o metodo
        return self.saldo  # restituisce un valore
    def get_lista_movimenti(self):  # definisce una funzione o metodo
        return self.lista_movimenti  # restituisce un valore