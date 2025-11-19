import os
import sys
import subprocess
import tkinter as tk
os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
class interfaccia:
    def __init__(self, root):
        self.root = root
        self.root.geometry("320x330")
        self_frame = tk.Frame(self.root, padx=10, pady=10)
        self_frame.pack()
        self.codice_label = tk.Label(self_frame, text="Codice prodotto")
        self.codice_label.pack(pady=5)
        self.codice_entry = tk.Entry(self_frame, width=30)
        self.codice_entry.pack(pady=5)
        self.quantita_label = tk.Label(self_frame, text="Quantità")
        self.quantita_label.pack(pady=5)
        self.quantita_entry = tk.Entry(self_frame, width=30)
        self.quantita_entry.pack(pady=5)
        self.compra_button = tk.Button(self_frame, text="Compra prodotto", command=self.compra)
        self.compra_button.pack(pady=10)
        self.output_text = tk.Label(self_frame, text="")
        self.output_text.pack(pady=5)

    # --- FUNZIONE CENTRALE ---
    def compra(self):
        codice = self.codice_entry.get()
        quantita = self.quantita_entry.get()

        if codice == "" or quantita == "":
            self.output_text.config(text="Inserisci codice e quantità.")
            return

        # Percorso del programma Java
        percorso_java = os.path.join("java_processor", "src")
        percorso_dir = os.path.join("java_processor", "src")

        try:
            subprocess.run(["javac", "-d", "../bin", "App.java"], cwd=percorso_dir, check=True, capture_output=True, text=True)

            risultato = subprocess.run(["java", "App", codice, quantita],
                                       cwd=percorso_dir,
                                       capture_output=True,
                                       text=True)

            # Mostra il risultato
            output = risultato.stdout.strip()
          #  if output == "":
           #     self.output_text.config(text="Nessuna risposta dal programma.")
           # else:
            self.output_text.config(text=output)

        except subprocess.CalledProcessError:
            self.output_text.config(text="Errore durante l'esecuzione Java.")
        except Exception as e:
            self.output_text.config(text=f"Errore imprevisto: {str(e)}")



def main():
    root = tk.Tk()
    app = interfaccia(root)
    root.mainloop()

main()
