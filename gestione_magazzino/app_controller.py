import os
import sys
import subprocess
import tkinter as tk
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("sigma")
        self.root.geometry("600x310")
        self_frame = tk.Frame(self.root, padx=10, pady=10)
        self_frame.pack()
        self.codice = tk.Label(self_frame, text="Codice prodotto")
        self.codice.pack(pady=5)
        self.codice = tk.Entry(self_frame, width=30)
        self.codice.pack(pady=5)
        self.quantita = tk.Label(self_frame, text="Quantità")
        self.quantita.pack(pady=5)
        self.quantita = tk.Entry(self_frame, width=30)
        self.quantita.pack(pady=5)
        self.compra = tk.Button(self_frame, text="Compra", command=self.compra)
        self.compra.pack(pady=10)
        self.risposta = tk.Label(self_frame, text="")
        self.risposta.pack(pady=5)

    def compra(self):
        codice = self.codice.get()
        quantita = self.quantita.get()
        out = java(codice, quantita)
        if out.startswith("ERRORE"):
            self.risposta.config(text="Errore 1: ")
        else:
            out = out.split(";")
            prodotto = Prodotto(out[0], out[1])
            self.risposta.config(text=f"Prodotto: {out[0]}, Quantità: {quantita}, Prezzo: {out[1]}, TOTALE: €{prodotto.calcolaTotale(int(quantita))}")

def java(prodotto, quantita):
    java_path = "./java_processor/src"
    # compile using UTF-8 encoding to handle accented characters
    compile = ["javac", "-encoding", "UTF-8", "-d", "../bin", "App.java"]
    compilatore = subprocess.run(
        compile,
        cwd=java_path,
        capture_output=True,
        text=True
    )
    class_path = "./java_processor/bin"
    if compilatore.returncode != 0:
        print("Errore 2")
        sys.exit()
    if prodotto and quantita:
        risultato = ["java", "App", prodotto, quantita]
    else:
        risultato = ["java", "App"]

    result_process = subprocess.run(
        risultato,
        cwd=class_path,
        capture_output=True,
        text=True
    )
    fine=result_process.stdout.strip()
    if fine:
        return fine

class Prodotto:
    def __init__(self, desc, price):
        self.desc = desc
        self.price = price
    def calcolaTotale(self, quantitaVenduta):
        return int(self.price) * int(quantitaVenduta)


def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

main()