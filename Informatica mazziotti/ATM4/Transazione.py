import datetime  # importa moduli necessari

# formatta la transazione in una stringa leggibile
class Transazione:  # definisce una classe
    def __init__(self, tipo_operazione = "N/A", importo = 0, saldo_post_operazione = 0):  # importa moduli necessari
        self.data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # assegna un valore a una variabile
        self.tipo_operazione = tipo_operazione  # assegna un valore a una variabile
        self.importo = importo  # importa moduli necessari
        self.saldo_post_operazione = saldo_post_operazione  # assegna un valore a una variabile
    def __str__(self):  # definisce una funzione o metodo
        return f"[{self.data_ora}] {self.tipo_operazione}: {self.importo:.2f} EUR | Saldo: {self.saldo_post_operazione:.2f} EUR"  # importa moduli necessari