from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Classe abstrata
class Afiliado(ABC):
    def __init__(self, nome, ID, contato, categoria):
        self.nome = nome
        self.ID = ID
        self.contato = contato
        self.categoria = categoria

    @abstractmethod
    def tipo(self):
        pass

class Fornecedor(Afiliado):  # Ex-cachorro
    def tipo(self):
        return "Fornecedor"

class Comprador(Afiliado):  # Ex-gato
    def tipo(self):
        return "Comprador"


# Lista para armazenar os cadastros afiliados
afiliados = []

def cadastrar_afiliados():
    nome = entrada_nome.get()
    ID = entrada_ID.get()
    contato = entrada_contato.get()
    categoria = var_tipo.get()

    if any(campo == "" for campo in (nome, contato)):
        messagebox.showerror("Falha", "Por favor preencha todos os campos.")
        return
    try:
        ID = int(ID)  # Verifica se o ID é um número
    except ValueError:
        messagebox.showerror("Falha", "O ID deve ser um número.")
        return

    if categoria == "Comprador":  # Criação do objeto do tipo gato
        afiliado = Comprador(nome, ID, contato, categoria)
    elif categoria == "Fornecedor":  # Criação do objeto do tipo cachorro
        afiliado = Fornecedor(nome, ID, contato, categoria)
    else:
        messagebox.showerror("Falha", "Selecione uma categoria de afiliado.")
        return

    messagebox.showinfo("Sucesso", f"{categoria} cadastrado com sucesso.")
    afiliados.append(afiliado)  # Adiciona o objeto à lista e exibe uma mensagem de sucesso.

# Função para atualizar a lista de afiliados
def atualizar_lista():
    lista_afiliados.delete(*lista_afiliados.get_children())  # Limpa a lista
    for i, afiliado in enumerate(afiliados, start=1):
        lista_afiliados.insert("", "end", values=(i, afiliado.categoria, afiliado.nome, afiliado.ID, afiliado.contato))

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de afiliados")
janela.geometry("600x400")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

abas = ttk.Notebook(janela)
abas.grid(row=0, column=0, sticky="nsew")
aba_cadastro = ttk.Frame(abas)

abas.add(aba_cadastro, text="Cadastro de afiliados")
aba_cadastro.rowconfigure([0, 1, 2, 3, 4], weight=1)
aba_cadastro.columnconfigure([0, 1], weight=1)

# Opções de dados
aba_cadastro.grid_columnconfigure(0, weight=0)  # Coluna do Label fixo
aba_cadastro.grid_columnconfigure(1, weight=1)  # Coluna do Entry ajustável

ttk.Label(aba_cadastro, text="Categoria:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
var_tipo = tk.StringVar(value="")

# Opções de categoria
radio_fornecedor = ttk.Radiobutton(aba_cadastro, text="Fornecedor", variable=var_tipo, value="Fornecedor")
radio_fornecedor.grid(row=0, column=1, sticky="w", padx=10)

radio_comprador = ttk.Radiobutton(aba_cadastro, text="Comprador", variable=var_tipo, value="Comprador")
radio_comprador.grid(row=0, column=1, sticky="e", padx=10)

ttk.Label(aba_cadastro, text="Nome:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
entrada_nome = ttk.Entry(aba_cadastro, font=("Arial", 12))
entrada_nome.grid(row=1, column=1, sticky="we", padx=5, pady=5)

ttk.Label(aba_cadastro, text="ID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
entrada_ID = ttk.Entry(aba_cadastro, font=("Arial", 12))
entrada_ID.grid(row=2, column=1, sticky="we", padx=5, pady=5)

ttk.Label(aba_cadastro, text="Contato:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)
entrada_contato = ttk.Entry(aba_cadastro, font=("Arial", 12))
entrada_contato.grid(row=3, column=1, sticky="we", padx=10, pady=5)

# Botão de cadastro
botao_cadastrar = ttk.Button(aba_cadastro, text="Cadastrar", command=cadastrar_afiliados)
botao_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)

# Aba da lista
aba_lista = ttk.Frame(abas)
abas.add(aba_lista, text="Lista")
aba_lista.rowconfigure(0, weight=1)
aba_lista.columnconfigure(0, weight=1)

# Aba dos cadastros
colunas = ("#", "Categoria", "Nome", "ID", "Contato")
lista_afiliados = ttk.Treeview(aba_lista, columns=colunas, show="headings")
for col in colunas:
    lista_afiliados.heading(col, text=col)
    lista_afiliados.column(col, anchor="center")

lista_afiliados.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Botão para atualizar a lista
botao_atualizar = ttk.Button(aba_lista, text="Atualizar Lista", command=atualizar_lista)
botao_atualizar.grid(row=1, column=0, pady=10)

janela.mainloop()
