import os  # importa moduli necessari
import random  # importa moduli necessari
from Banca import Banca  # importa moduli necessari
from Persona import Persona  # importa moduli necessari
from SportelloBancomat import SportelloBancomat  # importa moduli necessari

# Imposta la directory corrente
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # accede a un attributo o metodo

# main
try:  # tenta di eseguire codice che può generare errori
    banca = Banca("BancaMain")  # assegna un valore a una variabile
    if os.path.isfile("banca_dati.pkl"):  # verifica una condizione
        banca.carica_dati("banca_dati.pkl")  # accede a un attributo o metodo
        # Istanziamento di SportelloBancomat con l'istanza di banca
        sportello = SportelloBancomat(banca)   # assegna un valore a una variabile
        # Aggiunta di un check per evitare IndexError nel caso non ci siano clienti dopo il caricamento
        if banca.clienti:  # verifica una condizione
            # Stampa delle credenziali di accesso (solo a scopo di test)
            if len(banca.clienti) >= 2:  # verifica una condizione
                print(banca.clienti[0].carta.codice_carta, banca.clienti[0].carta.pin, banca.clienti[1].carta.codice_carta, banca.clienti[1].carta.pin)  # stampa un messaggio
            else:  # esegue in caso contrario
                print(banca.clienti[0].carta.codice_carta, banca.clienti[0].carta.pin)  # stampa un messaggio
    else:  # esegue in caso contrario
        # Creazione di clienti di esempio se il file non esiste
        cliente1 = Persona("Mario", "Rossi")  # assegna un valore a una variabile
        cliente2 = Persona("Anna", "Verdi")  # assegna un valore a una variabile
        banca.aggiungi_cliente(cliente1)  # accede a un attributo o metodo
        banca.aggiungi_cliente(cliente2)  # accede a un attributo o metodo
        print(f"Creato cliente: {cliente1.nome} {cliente1.cognome}, Carta: {cliente1.carta.codice_carta}, PIN: {cliente1.carta.pin}")  # stampa un messaggio
        print(f"Creato cliente: {cliente2.nome} {cliente2.cognome}, Carta: {cliente2.carta.codice_carta}, PIN: {cliente2.carta.pin}")  # stampa un messaggio
        
        banca.salva_dati("banca_dati.pkl")  # accede a un attributo o metodo
        # Istanziamento di SportelloBancomat con l'istanza di banca
        sportello = SportelloBancomat(banca)  # assegna un valore a una variabile
except Exception as e:  # gestisce un errore
    print(f"Errore nel caricamento dei dati o nell'esecuzione: {e}")  # stampa un messaggio
