import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Python sta partendo da: {os.getcwd()}")
java_path = './compito05_11/src'

compile = ['javac', '-d', './compito05_11/bin', 'App.java']

compile_process = subprocess.run(
    compile,
    cwd=java_path,
    capture_output=True,
    text=True
)

if compile_process.returncode != 0:
    print("Impossibil compilare")
    sys.exit()

class_path = './compito05_11/bin'

execution = ['java', 'App', '123']

result = subprocess.run(
    execution,
    cwd=class_path,
    capture_output=True,
    text=True
)

print(result.stdout)

if result.stderr:
    print(f"errors: {result.stderr}")



finestra = tk.Tk()
finestra.title("Gestione Utenti")
finestra.geometry("400x400")

titolo = tk.Label(finestra, text="Gestione Utenti", font=("Arial", 16, "bold"))
titolo.pack(pady=10)

frame_input = tk.Frame(finestra)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nome:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nome = tk.Entry(frame_input, width=25)
entry_nome.grid(row=0, column=1)

tk.Label(frame_input, text="Cognome:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_cognome = tk.Entry(frame_input, width=25)
entry_cognome.grid(row=1, column=1)

tk.Label(frame_input, text="Età:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_eta = tk.Entry(frame_input, width=25)
entry_eta.grid(row=2, column=1)

frame_bottoni = tk.Frame(finestra)
frame_bottoni.pack(pady=10)

btn_aggiungi = tk.Button(frame_bottoni, text="Aggiungi Utente", command=aggiungi_utente, width=15, bg="#4CAF50", fg="white")
btn_aggiungi.grid(row=0, column=0, padx=5)

btn_visualizza = tk.Button(frame_bottoni, text="Visualizza Utenti", command=visualizza_utenti, width=15, bg="#2196F3", fg="white")
btn_visualizza.grid(row=0, column=1, padx=5)

frame_output = tk.LabelFrame(finestra, text="Elenco Utenti", padx=10, pady=10)
frame_output.pack(padx=10, pady=10, fill="both", expand=True)

text_area = tk.Text(frame_output, height=10, width=45)
text_area.pack()

# Avvio dell'app
finestra.mainloop()