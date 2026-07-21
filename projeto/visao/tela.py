# visao/tela.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from modelo.cores import CORES_MAP


class TelaDesenho(tk.Tk):
    """Componente de Visão (Interface Gráfica Tkinter)."""

    def __init__(self):
        super().__init__()
        self.title("Desenho OO - Projeto MVC")
        self.geometry("800x680")

        # Atributos de instância declarados aqui, para que quem leia o
        # __init__ já saiba qual é a "forma" completa do objeto, sem
        # precisar entrar em criar_widgets() para descobrir. O método
        # abaixo apenas os PREENCHE, não os origina.
        self.barra_menu = None
        self.menu_arquivo = None
        self.frame_botoes = None
        self.menu_tipo = None
        self.tipo_figura_var = None
        self.cor_borda_var = None
        self.vai_preencher = None
        self.cor_preench_var = None
        self.canvas = None

        self.criar_widgets()

    def criar_widgets(self):
        self.criar_menu()

        self.frame_botoes = tk.Frame(self, bg="#f0f0f0")
        self.frame_botoes.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

        paddings = {'padx': 5, 'pady': 5}
        nomes_cores = list(CORES_MAP.keys())

        # Tipo de figura
        ttk.Label(self.frame_botoes, text='Tipo:').pack(side=tk.LEFT, **paddings)
        self.tipo_figura_var = tk.StringVar(self, value='Linha')
        self.menu_tipo = ttk.OptionMenu(self.frame_botoes, self.tipo_figura_var, 'Linha',
                                         'Linha', 'Rabisco', 'Círculo', 'Retângulo', 'Oval', 'Polígono Regular')
        self.menu_tipo.pack(side=tk.LEFT, **paddings)

        # Cor da borda
        ttk.Label(self.frame_botoes, text='Borda:').pack(side=tk.LEFT, **paddings)
        self.cor_borda_var = tk.StringVar(self, value='Preto')
        ttk.OptionMenu(self.frame_botoes, self.cor_borda_var, 'Preto', *nomes_cores).pack(side=tk.LEFT, **paddings)

        # Preenchimento Checkbutton
        self.vai_preencher = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.frame_botoes, text="Preencher", variable=self.vai_preencher).pack(side=tk.LEFT, **paddings)

        # Cor do preenchimento
        ttk.Label(self.frame_botoes, text='Cor Preenchimento:').pack(side=tk.LEFT, **paddings)
        self.cor_preench_var = tk.StringVar(self, value='Vermelho')
        ttk.OptionMenu(self.frame_botoes, self.cor_preench_var, 'Vermelho', *nomes_cores).pack(side=tk.LEFT, **paddings)

        # Canvas para desenho
        self.canvas = tk.Canvas(self, bg='white', cursor='cross')
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def criar_menu(self):
        """Cria só a estrutura do menu "Arquivo". Os comandos (o que cada
        item faz) são ligados pelo Controlador em conectar_eventos(), para
        que a View não precise conhecer a lógica de Salvar/Abrir."""
        self.barra_menu = tk.Menu(self)
        self.menu_arquivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.config(menu=self.barra_menu)

    def perguntar_caminho_salvar(self):
        """Abre o diálogo 'Salvar como' e retorna o caminho escolhido, ou
        None se o usuário cancelar."""
        caminho = filedialog.asksaveasfilename(
            title="Salvar desenho",
            defaultextension=".json",
            filetypes=[("Desenho (JSON)", "*.json"), ("Todos os arquivos", "*.*")],
        )
        return caminho or None

    def perguntar_caminho_abrir(self):
        """Abre o diálogo 'Abrir' e retorna o caminho escolhido, ou None se
        o usuário cancelar."""
        caminho = filedialog.askopenfilename(
            title="Abrir desenho",
            filetypes=[("Desenho (JSON)", "*.json"), ("Todos os arquivos", "*.*")],
        )
        return caminho or None

    def exibir_erro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def obter_configuracoes(self):
        """Retorna os dados do estado atual do cabeçalho de opções."""
        tipo = self.tipo_figura_var.get()
        c_borda = CORES_MAP[self.cor_borda_var.get()]
        c_preenchimento = CORES_MAP[self.cor_preench_var.get()] if self.vai_preencher.get() else None
        return tipo, c_borda, c_preenchimento

    def renderizar(self, desenho):
        """Atualiza visualmente o canvas com o estado do modelo."""
        self.canvas.delete("all")

        for figura in desenho.figuras:
            figura.desenhar(self.canvas)

        if desenho.figura_nova:
            desenho.figura_nova.desenhar_preview(self.canvas)
