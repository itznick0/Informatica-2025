import os
import sys
import subprocess
import tkinter as tk

    
class interfaccia:
    def __init__(self, root):
        self.root = root
        self.root.geometry("320x330")
        self_frame = tk.Frame(self.root, padx=10, pady=10)
        self_frame.pack()
        self.name_label = tk.Label(self_frame, text="Nome")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self_frame, width=30)
        self.name_entry.pack(pady=5)
        self.sname_label = tk.Label(self_frame, text="Cognome")
        self.sname_label.pack(pady=5)
        self.sname_entry = tk.Entry(self_frame, width=30)
        self.sname_entry.pack(pady=5)
        self.age_label = tk.Label(self_frame, text="Età")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self_frame, width=30)
        self.age_entry.pack(pady=5)
        self.add_button = tk.Button(self_frame, text="Aggiungi Utente", command=self.add)
        self.add_button.pack(pady=10)
        self.show_button = tk.Button(self_frame, text="Mostra Utenti", command=self.show)
        self.show_button.pack(pady=10)
        self.output_text = tk.Label(self_frame, text="")
        self.output_text.pack(pady=5)

    def add(self):
        name = self.name_entry.get()
        sname = self.sname_entry.get()
        age = self.age_entry.get()
        java_w(name, sname, age)
    
    def show(self):
        result = java_r()
        if result:
            formatted_result = ""
            lines = result.strip().split('\n')
            for line in lines:
                parts = line.split(';')
                if len(parts) == 3:
                    formatted_result += f"Nome: {parts[0]}, Cognome: {parts[1]}, Età: {parts[2]}\n"
            self.output_text.config(text=formatted_result)
        else:
            self.output_text.config(text='Errore')

def java_r():
    java_path = "./lettura/src"
    # compile using UTF-8 encoding to handle accented characters
    compile = ["javac", "-encoding", "UTF-8", "-d", "../bin", "App.java"]
    compile_process = subprocess.run(
        compile,
        cwd=java_path,
        capture_output=True,
        text=True
    )
    class_path = "./lettura/bin"
    if compile_process.returncode != 0:
        print("Compilation failed")
        sys.exit()
    result = ["java", "App"]
    result_process = subprocess.run(
        result,
        cwd=class_path,
        capture_output=True,
        text=True
    )

    if result_process.stdout:
        return result_process.stdout

def java_w(arg1, arg2, arg3):
    java_path = "./scrittura/src"
    # compile using UTF-8 encoding to handle accented characters
    compile = ["javac", "-encoding", "UTF-8", "-d", "../bin", "App.java"]
    compile_process = subprocess.run(
        compile,
        cwd=java_path,
        capture_output=True,
        text=True
    )
    class_path = "./scrittura/bin"
    if compile_process.returncode != 0:
        print("Compilation failed")
        sys.exit()
    if arg1 and arg2 and arg3 :
        result = ["java", "App", arg1, arg2, arg3]
    else:
        result = ["java", "App"]

    result_process = subprocess.run(
        result,
        cwd=class_path,
        capture_output=True,
        text=True
    )
    if result_process.stdout:
        return result_process.stdout


def main():
    root = tk.Tk()
    app = interfaccia(root)
    root.mainloop()

main()