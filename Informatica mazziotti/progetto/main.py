import tkinter as tk
from tkinter import messagebox
import subprocess

#funzionina onos
def salva_utente():
    nome = entry_nome.get().strip()
    cognome = entry_cognome.get().strip()
    eta = entry_eta.get().strip()

    if not nome or not cognome or not eta:
        messagebox.showwarning("Attenzione", "Compila tutti i campi!")
        return

    try:
        risultato = subprocess.run(
            ["java", "-cp", "progetti/scrittura/src", "App", nome, cognome, eta],
            capture_output=True,
            text=True
        )
        text_area.insert(tk.END, risultato.stdout + "\n")
        if risultato.stderr:
            text_area.insert(tk.END, "Errore: " + risultato.stderr + "\n")
    except Exception as e:
        text_area.insert(tk.END, f"Errore di esecuzione: {e}\n")

#interfacciosa
finestra = tk.Tk()
finestra.title("Gestione Anagrafica (Python + Java)")
finestra.geometry("500x400")
finestra.resizable(False, False)

frame_input = tk.Frame(finestra)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_input)
entry_nome.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Cognome:").grid(row=1, column=0, padx=5, pady=5)
entry_cognome = tk.Entry(frame_input)
entry_cognome.grid(row=1, column=1, padx=5)

tk.Label(frame_input, text="Età:").grid(row=2, column=0, padx=5, pady=5)
entry_eta = tk.Entry(frame_input)
entry_eta.grid(row=2, column=1, padx=5)

frame_bottoni = tk.Frame(finestra)
frame_bottoni.pack(pady=10)

btn_salva = tk.Button(frame_bottoni, text="Salva Utente", command=salva_utente)
btn_salva.grid(row=0, column=0, padx=10)

btn_mostra = tk.Button(frame_bottoni, text="Mostra Utenti", command=mostra_utenti)
btn_mostra.grid(row=0, column=1, padx=10)

text_area = tk.Text(finestra, height=12, width=60)
text_area.pack(pady=10)

finestra.mainloop()