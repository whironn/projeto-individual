from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Classe abstrata
class Afiliado(ABC):
    def __init__(self, nome, ID, contato, categoria, status, filial, data_de_emissao):
        self.nome = nome
        self.ID = ID
        self.contato = contato
        self.categoria = categoria
        self.status = status
        self.filial = filial
        self.data_de_emissao = data_de_emissao
    @abstractmethod
    def tipo(self):
        pass

class Fornecedor(Afiliado): 
    def tipo(self):
        return "Fornecedor"

class Comprador(Afiliado):
    def tipo(self):
        return "Comprador"

# Lista para armazenar os cadastros afiliados
afiliados = []

def cadastrar_afiliados():
    nome = entrada_nome.get()
    ID = entrada_ID.get()
    contato = entrada_contato.get()
    categoria = var_categoria.get()
    status = var_status.get()
    filial = entrada_filial.get()
    data_de_emissao = entrada_data_de_emissao.get()

    if any(campo == "" for campo in (nome, contato, status, filial, data_de_emissao)):
        messagebox.showerror("Falha", "Por favor preencha todos os campos.")
        return
    
    try:
        ID = int(ID)  # Verifica se o ID é um número
    except ValueError:
        messagebox.showerror("Falha", "O ID deve ser um número.")
        return
    
    # Validação do status
    if status == "Finalizada":
        pass  
    elif status == "No prazo":
        pass
    elif status == "Atrasada":
        pass 
    else:
        messagebox.showerror("Falha", "Status inválido. Escolha: Finalizada, No prazo ou Atrasada.")
        return
     
    # Criação do objeto conforme a categoria
    if categoria == "Comprador": 
        afiliado = Comprador(nome, ID, contato, categoria, status, filial, data_de_emissao)
    elif categoria == "Fornecedor":  
        afiliado = Fornecedor(nome, ID, contato, categoria, status, filial, data_de_emissao)
    else:
        messagebox.showerror("Falha", "Selecione uma categoria de afiliado.")
        return

    messagebox.showinfo("Sucesso", f"{categoria} cadastrado com sucesso.")
    afiliados.append(afiliado)  # Adiciona o objeto à lista de afiliados

# Função para atualizar a lista de afiliados
def atualizar_lista():
    lista_afiliados.delete(*lista_afiliados.get_children())  # Limpa a lista
    for i, afiliado in enumerate(afiliados, start=1):
        lista_afiliados.insert("", "end", values=(
            i, afiliado.ID, afiliado.filial, afiliado.categoria, afiliado.nome, 
            afiliado.status, afiliado.data_de_emissao, afiliado.contato
        ))

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
aba_cadastro.grid_columnconfigure(0, weight=0)
aba_cadastro.grid_columnconfigure(1, weight=0)
aba_cadastro.grid_columnconfigure(2, weight=0)

ttk.Label(aba_cadastro, text="Categoria:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
var_categoria = tk.StringVar(value="")

# Opções de categoria
radio_fornecedor = ttk.Radiobutton(aba_cadastro, text="Fornecedor", variable=var_categoria, value="Fornecedor")
radio_fornecedor.grid(row=0, column=1, sticky="w", padx=10)

radio_comprador = ttk.Radiobutton(aba_cadastro, text="Comprador", variable=var_categoria, value="Comprador")
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

# Status 
ttk.Label(aba_cadastro, text="Status:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=10, pady=5)
var_status = tk.StringVar(value="")

# Opções de status
radio_finalizada = ttk.Radiobutton(aba_cadastro, text="Finalizada", variable=var_status, value="Finalizada").grid(row=4, column=1, sticky="w", padx=10)
radio_no_prazo = ttk.Radiobutton(aba_cadastro, text="No prazo", variable=var_status, value="No prazo").grid(row=4, column=2, sticky="w", padx=10)
radio_atrasada = ttk.Radiobutton(aba_cadastro, text="Atrasada", variable=var_status, value="Atrasada").grid(row=4, column=3, sticky="w", padx=10)

ttk.Label(aba_cadastro, text="Filial:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=10, pady=5)
entrada_filial = ttk.Entry(aba_cadastro, font=("Arial", 12))  
entrada_filial.grid(row=5, column=1, sticky="we", padx=5, pady=5)

ttk.Label(aba_cadastro, text="Data de emissão:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=10, pady=5)
entrada_data_de_emissao = ttk.Entry(aba_cadastro, font=("Arial", 12))  
entrada_data_de_emissao.grid(row=6, column=1, sticky="we", padx=5, pady=5)

# Botão de cadastro
botao_cadastrar = ttk.Button(aba_cadastro, text="Cadastrar", command=cadastrar_afiliados).grid(row=7, column=1, sticky="nsew", columnspan=1, pady=5)

# Aba da lista
aba_lista = ttk.Frame(abas)
abas.add(aba_lista, text="Lista")
aba_lista.rowconfigure(0, weight=1)
aba_lista.columnconfigure(0, weight=1)

# Definindo a ordem correta das colunas
colunas = ("#", "ID", "Filial", "Categoria", "Nome", "Status", "Data de emissão", "Contato")
lista_afiliados = ttk.Treeview(aba_lista, columns=colunas, show="headings")

# Configuração das colunas do Treeview
for col in colunas:
    lista_afiliados.heading(col, text=col)
    lista_afiliados.column(col, anchor="center")

lista_afiliados.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Botão para atualizar a lista
botao_atualizar = ttk.Button(aba_lista, text="Atualizar Lista", command=atualizar_lista).grid(row=1, column=0, pady=10)

janela.mainloop()