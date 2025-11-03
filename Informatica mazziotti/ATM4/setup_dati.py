from Banca import Banca  # importa moduli necessari
from Persona import Persona  # importa moduli necessari
from BancomatPersonale import BancomatPersonale  # importa moduli necessari
from ContoCorrente import ContoCorrente  # importa moduli necessari
from Transazione import Transazione  # importa moduli necessari

# Crea l'oggetto Banca
banca = Banca("BancaMain")  # assegna un valore a una variabile

# Crea i clienti
cliente1 = Persona("Mario", "Rossi")  # assegna un valore a una variabile
cliente2 = Persona("Laura", "Bianchi")  # assegna un valore a una variabile

# Imposta i saldi iniziali e registra alcune transazioni iniziali
# Cliente 1
cliente1.carta.conto_associato.deposita(1000.00)  # accede a un attributo o metodo
cliente1.carta.conto_associato.preleva(50.00)  # accede a un attributo o metodo
banca.aggiungi_cliente(cliente1)  # accede a un attributo o metodo

# Cliente 2
cliente2.carta.conto_associato.deposita(500.00)  # accede a un attributo o metodo
banca.aggiungi_cliente(cliente2)  # accede a un attributo o metodo

# Salva l'oggetto Banca serializzato
banca.salva_dati('banca_dati.pkl')  # accede a un attributo o metodo
print(f"\nFile 'banca_dati.pkl' creato e salvato con successo.")  # stampa un messaggio

# Stampa le credenziali per il test
print("\n-------------------------------------------")  # stampa un messaggio
print("Clienti di Esempio Creati (utili per il test):")  # stampa un messaggio

print(f"\nCliente 1: {cliente1.nome} {cliente1.cognome}")  # stampa un messaggio
print(f"  Codice Carta: {cliente1.carta.codice_carta}")  # stampa un messaggio
print(f"  PIN: {cliente1.carta.pin}")  # stampa un messaggio
print(f"  Saldo Iniziale: {cliente1.carta.conto_associato.get_saldo():.2f} EUR")  # stampa un messaggio

print(f"\nCliente 2: {cliente2.nome} {cliente2.cognome}")  # stampa un messaggio
print(f"  Codice Carta: {cliente2.carta.codice_carta}")  # stampa un messaggio
print(f"  PIN: {cliente2.carta.pin}")  # stampa un messaggio
print(f"  Saldo Iniziale: {cliente2.carta.conto_associato.get_saldo():.2f} EUR")  # stampa un messaggio
print("-------------------------------------------")  # stampa un messaggio
