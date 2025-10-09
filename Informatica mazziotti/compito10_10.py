import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Classi (invariate)
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

fratello_corrente = mario  # di default


# ----------------------------
# Funzioni per selezionare il fratello
# ----------------------------

def seleziona_mario():
    global fratello_corrente
    fratello_corrente = mario
    label_fratello.config(text="Fratello attivo: Mario Rossi", fg="green")


def seleziona_luigi():
    global fratello_corrente
    fratello_corrente = luigi
    label_fratello.config(text="Fratello attivo: Luigi Rossi", fg="purple")


# ----------------------------
# Funzioni principali
# ----------------------------

def aggiungi_soldi():
    try:
        somma = float(entry_somma.get())
    except ValueError:
        messagebox.showerror("Errore di Input", "Per favore, inserisci solo numeri validi.")
        return

    if fratello_corrente.metti_soldi(somma):
        entry_somma.delete(0, tk.END)
        aggiorna_saldo()
        label_messaggi.config(text=f"{fratello_corrente.nome} ha aggiunto {somma}€.", fg="green")
    else:
        messagebox.showerror("Errore", "La somma deve essere positiva.")


def controlla_saldo():
    saldo = fratello_corrente.controlla_risparmi()
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
# Interfaccia (solo con pack() semplice, come nei tuoi esempi)
# ----------------------------

root = tk.Tk()
root.title("Salvadanaio di Famiglia")
root.geometry("400x420")
root.configure(bg="lightblue")

# Titolo
label_titolo = tk.Label(root, text="Salvadanaio Condiviso", font=("Helvetica", 16))
label_titolo.pack()

# Istruzione
label_istruzione = tk.Label(root, text="Scegli il fratello:")
label_istruzione.pack()

# Pulsanti per selezionare il fratello (uno sotto l'altro, con pack() semplice)
button_mario = tk.Button(root, text="Mario Rossi", command=seleziona_mario, bg="lightgreen")
button_mario.pack()

button_luigi = tk.Button(root, text="Luigi Rossi", command=seleziona_luigi, bg="lightpink")
button_luigi.pack()

# Etichetta che mostra chi è attivo
label_fratello = tk.Label(root, text="Fratello attivo: Mario Rossi", font=("Helvetica", 10, "bold"), fg="green", bg="lightblue")
label_fratello.pack()

# Somma da aggiungere
label_somma = tk.Label(root, text="Somma da aggiungere (€):")
label_somma.pack()

entry_somma = tk.Entry(root)
entry_somma.pack()

# Pulsanti azioni
button_aggiungi = tk.Button(root, text="Aggiungi soldi", command=aggiungi_soldi, bg="green", fg="white")
button_aggiungi.pack()

button_controlla = tk.Button(root, text="Controlla saldo", command=controlla_saldo, bg="blue", fg="white")
button_controlla.pack()

button_svuota = tk.Button(root, text="Svuota salvadanaio", command=svuota_salvadanaio, bg="red", fg="white")
button_svuota.pack()

# Saldo
label_saldo = tk.Label(root, text="Saldo attuale: 0€", font=("Helvetica", 14), fg="darkgreen", bg="lightblue")
label_saldo.pack()

# Messaggi
label_messaggi = tk.Label(root, text="", font=("Helvetica", 10), bg="lightblue")
label_messaggi.pack()

root.mainloop()