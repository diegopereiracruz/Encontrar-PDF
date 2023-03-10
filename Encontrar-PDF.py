import tkinter as tk
from tkinter import filedialog
from tkinter import END
import os
import PyPDF2
import platform
import subprocess

PLATFORM_WINDOWS = platform.system() == "Windows"

path = os.getcwd() # Obtém o caminho atual
print(path)

def open_file(event): # Executa a ação de abrir o arquivo encontrado
    item = listbox.get(listbox.curselection())
    if PLATFORM_WINDOWS:
        os.startfile(item)
    else:
        subprocess.call(["xdg-open", item])

def search_files(path, word):
    result = []
    listbox.delete(0,END)

    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            filepath = os.path.join(path, filename)
            pdfFileObj = open(filepath, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)

            for i in range(0, len(pdfReader.pages)):
                    pageObj = pdfReader.pages[i]
                    texto = pageObj.extract_text().lower()
                    if word.lower() in texto or word.upper() in texto or word.capitalize() in texto:
                        #result.append(file)
                        result.append(filepath)
                        break

    if len(result) == 0:
        result.append("Não foi encontrado")
        return result
    
    else:
        return list(set(result))

def on_search(): # Inicia a função de busca
    word = search_entry.get()
    global path
    print(path)
    result = search_files(path, word)
    #print(result)
    for item in result:
        listbox.insert(tk.END, item)

def set_path():
    global path
    path = filedialog.askdirectory() # Janela de seleção de pasta
    print(path)

root = tk.Tk() # Itera o pacote Tkinter
root.title("Encontrar PDF")

# Elementos: Texto, Caixa de Texto, Botão...
search_label = tk.Label(root, text="Encontrar PDF pela palavra-chave ou frase")
search_entry = tk.Entry(root, width=70)
search_entry.focus_force()
path_button = tk.Button(root, text="Escolher pasta...", command=set_path, width=12)
search_button = tk.Button(root, text="Pesquisar", command=on_search, width=10)
listbox = tk.Listbox(root)
listbox.pack()
author_label = tk.Label(root, text="github.com/diegopereiracruz")
listbox.bind("<Double-Button-1>", open_file) # Abrir arquivo com duplo clique

# Layout
search_label.pack(side="top", padx=(10, 0))
author_label.pack(side="top", padx=(10, 0))
path_button.pack(side="left", padx=(0, 0))
search_entry.pack(side="left", padx=(10, 0), fill="x", expand=True)
search_button.pack(side="left", padx=(10, 0))
listbox.pack(side="bottom", fill="both", expand=True)


root.mainloop()