import tkinter as tk  # importa moduli necessari
from tkinter import simpledialog  # importa moduli necessari

# interfaccia grafica

class SportelloBancomat:  # definisce una classe
    def __init__(self, banca_instance): # Aggiunto 'banca_instance' per l'accesso a 'banca'  # definisce una funzione o metodo
        self.banca = banca_instance  # assegna un valore a una variabile
        self.root = tk.Tk()  # assegna un valore a una variabile
        self.root.withdraw()  # accede a un attributo o metodo
        self.dimensione="300x150+100+100"  # assegna un valore a una variabile
        self.build_login_GUI(self.root, self.dimensione)  # accede a un attributo o metodo
        self.root.mainloop()  # accede a un attributo o metodo

    def build_login_GUI(self, root, dimensione):  # definisce una funzione o metodo
        self.finestra_login = tk.Toplevel(root)  # assegna un valore a una variabile
        self.finestra_login.title("Login Bancomat")  # accede a un attributo o metodo
        self.finestra_login.geometry(dimensione)  # tenta di eseguire codice che può generare errori
        for i in range(4):  # itera su una sequenza
            root.grid_columnconfigure(i, weight=1)  # assegna un valore a una variabile
        for i in range(5):  # itera su una sequenza
            root.grid_rowconfigure(i, weight=1)  # assegna un valore a una variabile
        
        self.codice_carta = tk.Entry(self.finestra_login, font=("Arial", 12))  # tenta di eseguire codice che può generare errori
        self.codice_carta.grid(row=0, column=0, columnspan=4, pady=(10, 5), sticky="s")  # assegna un valore a una variabile
        self.pin_carta = tk.Entry(self.finestra_login, font=("Arial", 12))  # tenta di eseguire codice che può generare errori
        self.pin_carta.grid(row=1, column=0, columnspan=4, pady=(5, 10), sticky="s")  # assegna un valore a una variabile
        
        tk.Button(self.finestra_login, text="Accedi", command=self.accedi_handler, font=("Arial", 10), bg="#b1d7ff").grid(row=2, column=0, columnspan=4, pady=(10, 5), sticky="s")  # assegna un valore a una variabile

        self.messaggi = tk.Label(self.finestra_login, text="Benvenuto!", font=("Arial", 10), fg="red")  # assegna un valore a una variabile
        self.messaggi.grid(row=3, column=0, columnspan=4, pady=(5, 10), sticky="s")  # assegna un valore a una variabile
    def accedi_handler(self):  # definisce una funzione o metodo
        try:  # tenta di eseguire codice che può generare errori
            codice = int(self.codice_carta.get())  # assegna un valore a una variabile
            pin = int(self.pin_carta.get())  # assegna un valore a una variabile
            self.cliente = self.banca.cerca_cliente_da_carta(codice)  # assegna un valore a una variabile
            if self.cliente and self.cliente.carta.verifica_pin(pin):  # verifica una condizione
                self.finestra_login.destroy()  # accede a un attributo o metodo
                self.build_main_GUI(self.root, self.dimensione)  # accede a un attributo o metodo
            else:  # esegue in caso contrario
                self.messaggi.config(text="Codice o PIN non validi")  # assegna un valore a una variabile
        except ValueError:  # gestisce un errore
            self.messaggi.config(text="Inserisci numeri")  # assegna un valore a una variabile
    
    def build_main_GUI(self, root, dimensione):  # definisce una funzione o metodo
        self.finestra_main = tk.Toplevel(root)  # assegna un valore a una variabile
        self.finestra_main.title("Sportello Bancomat")  # accede a un attributo o metodo
        self.finestra_main.geometry(dimensione)  # tenta di eseguire codice che può generare errori
        for i in range(4):  # itera su una sequenza
            root.grid_columnconfigure(i, weight=1)  # assegna un valore a una variabile
        for i in range(6):  # itera su una sequenza
            root.grid_rowconfigure(i, weight=1)  # assegna un valore a una variabile

        tk.Label(self.finestra_main, text=f"Benvenuto {self.cliente.nome} {self.cliente.cognome}", font=("Arial", 12)).grid(row=0, column=0, columnspan=4, pady=(10, 5), sticky="s")  # assegna un valore a una variabile

        self.saldo = tk.Label(self.finestra_main, text=f"Saldo corrente: {self.cliente.carta.conto_associato.get_saldo():.2f} EUR", font=("Arial", 10))  # assegna un valore a una variabile
        self.saldo.grid(row=1, column=0, columnspan=4, pady=(5, 10), sticky="s")  # assegna un valore a una variabile

        tk.Button(self.finestra_main, text="Preleva", command=self.preleva_handler, font=("Arial", 10), bg="#b1d7ff").grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")  # assegna un valore a una variabile
        tk.Button(self.finestra_main, text="Versa", command=self.versa_handler, font=("Arial", 10), bg="#b1d7ff").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")  # assegna un valore a una variabile
        tk.Button(self.finestra_main, text="Lista Movimenti", command=self.movimenti_handler, font=("Arial", 10), bg="#b1d7ff").grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="ew")  # assegna un valore a una variabile
        tk.Button(self.finestra_main, text="Esci", command=self.esci_handler, font=("Arial", 10), bg="#ffb1b1").grid(row=5, column=0, columnspan=4, padx=5, pady=10, sticky="ew")  # assegna un valore a una variabile
        
    def preleva_handler(self):  # definisce una funzione o metodo
        input = simpledialog.askinteger("Preleva", "Inserisci l'importo da prelevare: ")  # importa moduli necessari
        if input:  # verifica una condizione
            self.cliente.carta.conto_associato.preleva(input)  # accede a un attributo o metodo
            self.banca.salva_dati('banca_dati.pkl')  # accede a un attributo o metodo
            self.saldo.config(text=f"Saldo corrente: {self.cliente.carta.conto_associato.get_saldo():.2f} EUR")  # assegna un valore a una variabile
    def versa_handler(self):  # definisce una funzione o metodo
        input = simpledialog.askinteger("Versa", "Inserisci l'importo da versare: ")  # importa moduli necessari
        if input:  # verifica una condizione
            self.cliente.carta.conto_associato.deposita(input)  # accede a un attributo o metodo
            self.banca.salva_dati('banca_dati.pkl')  # accede a un attributo o metodo
            self.saldo.config(text=f"Saldo corrente: {self.cliente.carta.conto_associato.get_saldo():.2f} EUR")  # assegna un valore a una variabile
    def movimenti_handler(self):  # definisce una funzione o metodo
        self.finestra_movimenti = tk.Toplevel(self.root)  # assegna un valore a una variabile
        self.finestra_movimenti.title("Lista Movimenti")  # accede a un attributo o metodo
        self.finestra_movimenti.geometry("400x300+150+150")  # tenta di eseguire codice che può generare errori
        self.lista_movimenti = self.cliente.carta.conto_associato.get_lista_movimenti()  # assegna un valore a una variabile
        for i in range(1):  # itera su una sequenza
            self.finestra_movimenti.grid_columnconfigure(i, weight=1)  # assegna un valore a una variabile
        # La riga qui sotto non è corretta per il layout a griglia:
        # for i in range(len(self.lista_movimenti)):
        #     self.finestra_movimenti.grid_columnconfigure(i, weight=1)
        # Manteniamo la logica originale di posizionamento:
        for idx, i in enumerate(self.lista_movimenti):  # itera su una sequenza
            tk.Label(self.finestra_movimenti, text=i.__str__(), font=("Arial", 10)).grid(row=idx, column=0, padx=5, pady=5, sticky="w")  # assegna un valore a una variabile

    def esci_handler(self):  # definisce una funzione o metodo
        self.finestra_main.destroy()  # accede a un attributo o metodo
        self.build_login_GUI(self.root, self.dimensione)  # accede a un attributo o metodo