from BancomatPersonale import BancomatPersonale  # importa moduli necessari

# persona che possiede la carta
class Persona:  # definisce una classe
    def __init__(self, nome, cognome):  # definisce una funzione o metodo
        self.nome = nome  # assegna un valore a una variabile
        self.cognome = cognome  # assegna un valore a una variabile
        self.carta = BancomatPersonale()  # assegna un valore a una variabile