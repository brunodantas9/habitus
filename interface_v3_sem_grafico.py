
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from package.user import Usuario
from package.categoria import Categoria
from package.habit import HabitoDiario, HabitoSemanal, HabitoMensal
from package.storage import salvar_dados, carregar_dados

class HabitusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habitus - Controle de Hábitos")
        self.usuario = carregar_dados()
        if not self.usuario:
            self.usuario = Usuario("Flávia")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # Botão de adicionar hábito
        self.botao_add = ttk.Button(self.frame, text="➕ Novo Hábito", command=self.abrir_modal_habito)
        self.botao_add.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Lista de hábitos
        self.lista_habitos = tk.Listbox(self.frame, width=80, height=12)
        self.lista_habitos.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Botões de ação
        self.botao_concluir = ttk.Button(self.frame, text="✔️ Marcar como feito", command=self.marcar_como_feito)
        self.botao_concluir.grid(row=2, column=0, padx=5, pady=5)

        self.botao_editar = ttk.Button(self.frame, text="✏️ Editar", command=self.editar_habito)
        self.botao_editar.grid(row=2, column=1, padx=5, pady=5)

        self.botao_excluir = ttk.Button(self.frame, text="🗑 Excluir", command=self.excluir_habito)
        self.botao_excluir.grid(row=2, column=2, padx=5, pady=5)

        self.status = tk.Label(self.frame, text="", fg="green")
        self.status.grid(row=3, column=0, columnspan=3)

        self.atualizar_lista()

    def abrir_modal_habito(self):
        modal = tk.Toplevel(self.root)
        modal.title("Cadastrar Novo Hábito")
        modal.geometry("400x300")

        tk.Label(modal, text="Nome:").pack()
        nome_entry = tk.Entry(modal, width=40)
        nome_entry.pack()

        tk.Label(modal, text="Descrição:").pack()
        descricao_entry = tk.Entry(modal, width=40)
        descricao_entry.pack()

        tk.Label(modal, text="Categoria:").pack()
        categoria_entry = tk.Entry(modal, width=40)
        categoria_entry.insert(0, "Pessoal")
        categoria_entry.pack()

        tk.Label(modal, text="Periodicidade:").pack()
        periodicidade_var = tk.StringVar()
        ttk.Combobox(modal, textvariable=periodicidade_var, values=["diário", "semanal", "mensal"]).pack()

        def salvar():
            nome = nome_entry.get().strip()
            descricao = descricao_entry.get().strip()
            categoria = categoria_entry.get().strip()
            periodo = periodicidade_var.get()

            if nome and periodo:
                cat = Categoria(categoria, "verde")
                if periodo == "diário":
                    hab = HabitoDiario(nome, descricao, cat, periodo)
                elif periodo == "semanal":
                    hab = HabitoSemanal(nome, descricao, cat, periodo)
                else:
                    hab = HabitoMensal(nome, descricao, cat, periodo)

                self.usuario.adicionar_habito(hab)
                salvar_dados(self.usuario)
                self.atualizar_lista()
                modal.destroy()
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos obrigatórios.")

        ttk.Button(modal, text="Salvar", command=salvar).pack(pady=10)

    def atualizar_lista(self):
        self.lista_habitos.delete(0, tk.END)
        for i, hab in enumerate(self.usuario.habitos):
            ultima = max(hab.registros) if hab.registros else "Nunca"
            linha = f"{i+1}. {hab.nome} [{hab.periodicidade}] - Progresso: {hab.progresso()} - Última: {ultima}"
            self.lista_habitos.insert(tk.END, linha)

    def marcar_como_feito(self):
        sel = self.lista_habitos.curselection()
        if sel:
            idx = sel[0]
            hab = self.usuario.habitos[idx]
            hab.registrar(date.today())
            salvar_dados(self.usuario)
            self.atualizar_lista()
        else:
            messagebox.showinfo("Aviso", "Selecione um hábito para marcar como feito.")

    def editar_habito(self):
        sel = self.lista_habitos.curselection()
        if not sel:
            messagebox.showinfo("Aviso", "Selecione um hábito para editar.")
            return

        idx = sel[0]
        hab = self.usuario.habitos[idx]

        modal = tk.Toplevel(self.root)
        modal.title("Editar Hábito")
        modal.geometry("400x300")

        tk.Label(modal, text="Nome:").pack()
        nome_entry = tk.Entry(modal, width=40)
        nome_entry.insert(0, hab.nome)
        nome_entry.pack()

        tk.Label(modal, text="Descrição:").pack()
        descricao_entry = tk.Entry(modal, width=40)
        descricao_entry.insert(0, hab.descricao)
        descricao_entry.pack()

        tk.Label(modal, text="Periodicidade:").pack()
        periodicidade_var = tk.StringVar(value=hab.periodicidade)
        ttk.Combobox(modal, textvariable=periodicidade_var, values=["diário", "semanal", "mensal"]).pack()

        def salvar_edicao():
            hab.nome = nome_entry.get().strip()
            hab.descricao = descricao_entry.get().strip()
            hab.periodicidade = periodicidade_var.get()
            salvar_dados(self.usuario)
            self.atualizar_lista()
            modal.destroy()

        ttk.Button(modal, text="Salvar", command=salvar_edicao).pack(pady=10)

    def excluir_habito(self):
        sel = self.lista_habitos.curselection()
        if sel:
            idx = sel[0]
            del self.usuario.habitos[idx]
            salvar_dados(self.usuario)
            self.atualizar_lista()

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitusApp(root)
    root.mainloop()
