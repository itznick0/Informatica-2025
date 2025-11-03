import pickle  # importa moduli necessari
from Persona import Persona  # importa moduli necessari

# la banca che gestisce i clienti
class Banca:  # definisce una classe
    def __init__(self, nome_banca):  # definisce una funzione o metodo
        self.nome_banca = nome_banca  # assegna un valore a una variabile
        self.clienti = []  # assegna un valore a una variabile
    def aggiungi_cliente(self, persona):  # definisce una funzione o metodo
        self.clienti.append(persona)  # accede a un attributo o metodo
    def cerca_cliente_da_carta(self, codice_carta):  # definisce una funzione o metodo
        for cliente in self.clienti:  # itera su una sequenza
            if cliente.carta.codice_carta == codice_carta:  # verifica una condizione
                return cliente  # restituisce un valore
    def salva_dati(self, file):  # definisce una funzione o metodo
        with open(file, "wb") as f:  # apre un file
            pickle.dump(self, f)  # accede a un attributo o metodo
    def carica_dati(self, file):  # definisce una funzione o metodo
        with open(file, "rb") as f:  # apre un file
            o = pickle.load(f)  # assegna un valore a una variabile
            self.clienti = o.clienti  # assegna un valore a una variabile
            self.nome_banca = o.nome_banca  # assegna un valore a una variabile