# controlador/controlador_desenho.py
from modelo.figuras import Linha, Retangulo, Oval, Circulo, Rabisco, PoligonoRegular
from modelo.persistencia import salvar_desenho, abrir_desenho

# Fábrica de estados: liga o texto do menu à classe (estado) correspondente.
# É a única "decisão de tipo" que sobra no sistema — tudo que acontece
# depois disso é resolvido por polimorfismo dentro de cada Figura.
_FABRICA_FIGURAS = {
    'Linha': lambda x, y, cb, cp: Linha(x, y, x, y, cb),
    'Retângulo': lambda x, y, cb, cp: Retangulo(x, y, x, y, cb, cp),
    'Oval': lambda x, y, cb, cp: Oval(x, y, x, y, cb, cp),
    'Círculo': lambda x, y, cb, cp: Circulo(x, y, 0, cb, cp),
    'Rabisco': lambda x, y, cb, cp: Rabisco([(x, y)], cb),
}


class ControladorDesenho:

    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao
        self.conectar_eventos()

    def conectar_eventos(self):
        # 1. Clique inicial do mouse
        self.visao.canvas.bind('<ButtonPress-1>', self.tratar_clique)

        # 2. Movimento sem segurar o botão (usado apenas para o preview do Polígono)
        self.visao.canvas.bind('<Motion>', self.atualizar_preview_poligono)

        # 3. Movimento SEGURANDO o botão (usado para Linha, Retângulo, Círculo, Rabisco, Oval)
        self.visao.canvas.bind('<B1-Motion>', self.atualizar_figura_arrasto)

        # 4. Soltar o botão do mouse (finaliza Linha, Retângulo, Círculo, Rabisco, Oval)
        self.visao.canvas.bind('<ButtonRelease-1>', self.finalizar_figura_arrasto)

        # 5. Duplo clique (finaliza apenas o Polígono)
        self.visao.canvas.bind('<Double-Button-1>', self.finalizar_poligono)

        # 6. Menu Arquivo > Salvar / Abrir
        self.visao.menu_arquivo.add_command(label="Salvar...", command=self.acao_salvar)
        self.visao.menu_arquivo.add_command(label="Abrir...", command=self.acao_abrir)

    def tratar_clique(self, event):
        tipo, c_borda, c_preenchimento = self.visao.obter_configuracoes()
        x, y = event.x, event.y
        figura_atual = self.modelo.figura_nova

        if tipo == 'Polígono Regular':
            if figura_atual is None:
                self.modelo.iniciar_figura(PoligonoRegular([(x, y)], c_borda, c_preenchimento))
            else:
                self.modelo.adicionar_ponto_atual(x, y)
        else:
            construtor = _FABRICA_FIGURAS[tipo]
            self.modelo.iniciar_figura(construtor(x, y, c_borda, c_preenchimento))

        self.visao.renderizar(self.modelo)

    def atualizar_preview_poligono(self, event):
        """<Motion> (sem clicar): só interessa a estados que se constroem por cliques."""
        figura = self.modelo.figura_nova
        if figura is not None and figura.interacao_por_cliques:
            self.modelo.atualizar_figura_atual(event.x, event.y)
            self.visao.renderizar(self.modelo)

    def atualizar_figura_arrasto(self, event):
        """<B1-Motion>: só interessa a estados de clique+arrasto (não o Polígono)."""
        figura = self.modelo.figura_nova
        if figura is None or figura.interacao_por_cliques:
            return
        self.modelo.atualizar_figura_atual(event.x, event.y)
        self.visao.renderizar(self.modelo)

    def finalizar_figura_arrasto(self, event):
        """<ButtonRelease-1>: finaliza tudo que não seja o Polígono."""
        figura = self.modelo.figura_nova
        if figura is not None and not figura.interacao_por_cliques:
            self.modelo.finalizar_figura_atual(event.x, event.y)
            self.visao.renderizar(self.modelo)

    def finalizar_poligono(self, event):
        """<Double-Button-1>: finaliza apenas o Polígono."""
        figura = self.modelo.figura_nova
        if figura is not None and figura.interacao_por_cliques:
            self.modelo.finalizar_figura_atual(event.x, event.y)
            self.visao.renderizar(self.modelo)

    def acao_salvar(self):
        """Pede um caminho à View, delega a gravação ao Modelo (persistencia.py)."""
        caminho = self.visao.perguntar_caminho_salvar()
        if not caminho:
            return
        try:
            salvar_desenho(self.modelo, caminho)
        except OSError as erro:
            self.visao.exibir_erro("Erro ao salvar", str(erro))

    def acao_abrir(self):
        """Pede um caminho à View, delega a leitura ao Modelo (persistencia.py)
        e, se der certo, substitui o desenho atual e re-renderiza."""
        caminho = self.visao.perguntar_caminho_abrir()
        if not caminho:
            return
        try:
            abrir_desenho(self.modelo, caminho)
        except (OSError, ValueError) as erro:
            self.visao.exibir_erro("Erro ao abrir", str(erro))
            return
        self.visao.renderizar(self.modelo)
