import random  # importa moduli necessari
from ContoCorrente import ContoCorrente  # importa moduli necessari

# la carta di una persona, associata a un conto
class BancomatPersonale:  # definisce una classe
    def __init__(self):  # definisce una funzione o metodo
        self.codice_carta = random.randint(10**15, 10**16 - 1)  # assegna un valore a una variabile
        self.pin = random.randint(10**4, 10**5 - 1)  # assegna un valore a una variabile
        self.conto_associato = ContoCorrente()  # assegna un valore a una variabile
    def verifica_pin(self, pin_inserito):  # definisce una funzione o metodo
        if pin_inserito == self.pin:  # verifica una condizione
            return True  # restituisce un valore