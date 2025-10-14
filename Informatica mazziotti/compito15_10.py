import tkinter as tk
from tkinter import messagebox

class Salvadanaio:
    def __init__(self):
        self.totale = 0
    def aggiungi(self, somma):
        if somma > 0:
            self.totale += somma
        else:
            messagebox.showerror("Errore:", "La somma deve essere positiva.")
    def mostra_saldo(self):
        return self.totale
    def svuota(self):
        self.totale = 0
class Fratello:
    def __init__(self, nome, cognome, salvadanaio_condiviso):
        self.nome = nome
        self.cognome = cognome
        self.salvadanaio_condiviso = salvadanaio_condiviso
        self.salvadanaio_personale = Salvadanaio()
    def metti_soldi_condiviso(self, somma):
        self.salvadanaio_condiviso.aggiungi(somma)
    def metti_soldi_personale(self, somma):
        self.salvadanaio_personale.aggiungi(somma)
def crea_finestra_salvadanaio(root, salvadanaio, titolo, posizione):
    finestra = tk.Toplevel(root)
    finestra.title(titolo)
    finestra.geometry("300x200")
    finestra.geometry(f"+{posizione[0]}+{posizione[1]}")
    finestra.configure(bg="#f0f0f0")
    label_titolo = tk.Label(finestra, text=titolo, bg="#4a7abc", fg="white", font=("Arial", 12, "bold"))
    label_titolo.pack()
    label_saldo = tk.Label(finestra, text=f"Saldo: {salvadanaio.mostra_saldo()}€", bg="#f0f0f0", font=("Arial", 10))
    label_saldo.pack(pady=10)
    def aggiorna_label():
        label_saldo.config(text=f"Saldo: €{salvadanaio.mostra_saldo()}")
    def metti_soldi():
        try:
            somma = int(entry.get())
            salvadanaio.aggiungi(somma)
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero valido.")
        aggiorna_label()
        entry.delete(0, tk.END)
    entry = tk.Entry(finestra, font=("Arial", 10))
    entry.pack(pady=5)
    btn_metti = tk.Button(finestra, text="Metti soldi", command=metti_soldi, bg="#4CAF50", fg="white", font=("Arial", 10))
    btn_metti.pack(pady=3)
    btn_visualizza = tk.Button(finestra, text="Visualizza saldo", command=aggiorna_label, bg="#2196F3", fg="white", font=("Arial", 10))
    btn_visualizza.pack(pady=3)
    def svuota_salvadanaio():
        salvadanaio.svuota()
        aggiorna_label()
    btn_svuota = tk.Button(finestra, text="Svuota salvadanaio", command=svuota_salvadanaio, bg="#f44336", fg="white", font=("Arial", 10))
    btn_svuota.pack(pady=3)
    return finestra
salvadanaio_famiglia = Salvadanaio()
mario = Fratello("Mario", "Rossi", salvadanaio_famiglia)
luigi = Fratello("Luigi", "Rossi", salvadanaio_famiglia)
root = tk.Tk()
root.geometry("1x1+-1000+-1000")
finestra_condivisa = crea_finestra_salvadanaio(root, salvadanaio_famiglia, "Salvadanaio Condiviso", (100, 100))
crea_finestra_salvadanaio(root, mario.salvadanaio_personale, f"Salvadanaio di {mario.nome}", (500, 100))
crea_finestra_salvadanaio(root, luigi.salvadanaio_personale, f"Salvadanaio di {luigi.nome}", (100, 400))
root.mainloop()