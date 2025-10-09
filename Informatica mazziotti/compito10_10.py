import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Classi del modello
# ----------------------------

class Salvadanaio:
    def __init__(self):
        self.totale = 0

    def aggiungi(self, somma):
        if somma > 0:
            self.totale += somma
            return True
        else:
            return False

    def mostra_saldo(self):
        return self.totale

    def svuota(self):
        self.totale = 0


class Fratello:
    def __init__(self, nome, cognome, salvadanaio):
        self.nome = nome
        self.cognome = cognome
        self.salvadanaio = salvadanaio

    def metti_soldi(self, somma):
        return self.salvadanaio.aggiungi(somma)

    def controlla_risparmi(self):
        return self.salvadanaio.mostra_saldo()


# ----------------------------
# Oggetti
# ----------------------------

salvadanaio_famiglia = Salvadanaio()
mario = Fratello("Mario", "Rossi", salvadanaio_famiglia)
luigi = Fratello("Luigi", "Rossi", salvadanaio_famiglia)


# ----------------------------
# Funzioni GUI
# ----------------------------

def aggiungi_soldi():
    try:
        somma = float(entry_somma.get())
    except ValueError:
        messagebox.showerror("Errore di Input", "Per favore, inserisci solo numeri validi.")
        return

    fratello_nome = fratello_selezionato.get()
    fratello = mario if fratello_nome == "Mario Rossi" else luigi

    if fratello.metti_soldi(somma):
        entry_somma.delete(0, tk.END)
        aggiorna_saldo()
        label_messaggi.config(text=f"{fratello.nome} ha aggiunto {somma}€.", fg="green")
    else:
        messagebox.showerror("Errore", "La somma deve essere positiva.")


def controlla_saldo():
    fratello_nome = fratello_selezionato.get()
    fratello = mario if fratello_nome == "Mario Rossi" else luigi
    saldo = fratello.controlla_risparmi()
    label_saldo.config(text=f"Saldo attuale: {saldo}€")
    label_messaggi.config(text="Saldo visualizzato.", fg="blue")


def svuota_salvadanaio():
    salvadanaio_famiglia.svuota()
    aggiorna_saldo()
    label_messaggi.config(text="Il salvadanaio è stato svuotato.", fg="orange")


def aggiorna_saldo():
    saldo = salvadanaio_famiglia.mostra_saldo()
    label_saldo.config(text=f"Saldo attuale: {saldo}€")


# ----------------------------
# Interfaccia
# ----------------------------

root = tk.Tk()
root.title("Salvadanaio di Famiglia")
root.geometry("400x350")
root.configure(bg="lightblue")

tk.Label(root, text="Salvadanaio Condiviso", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Seleziona un fratello:").pack()
fratello_selezionato = tk.StringVar(value="Mario Rossi")
tk.OptionMenu(root, fratello_selezionato, "Mario Rossi", "Luigi Rossi").pack(pady=5)

tk.Label(root, text="Somma da aggiungere (€):").pack()
entry_somma = tk.Entry(root)
entry_somma.pack(pady=5)

tk.Button(root, text="Aggiungi soldi", command=aggiungi_soldi, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Controlla saldo", command=controlla_saldo, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Svuota salvadanaio", command=svuota_salvadanaio, bg="red", fg="white").pack(pady=10)

label_saldo = tk.Label(root, text="Saldo attuale: 0€", font=("Helvetica", 14), fg="darkgreen")
label_saldo.pack(pady=10)

label_messaggi = tk.Label(root, text="", font=("Helvetica", 10), bg="lightblue")
label_messaggi.pack(pady=5)

root.mainloop()
